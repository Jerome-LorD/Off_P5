#!/usr/bin/env python
"""Download, clean and inserts datas into db."""
from settings import DB_NAME
import re
import logging

import requests
import mysql.connector

from typing import List


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Downloader:
    """Download and insert into DB."""

    def __init__(self, user, password):
        """Init."""
        self.user = user
        self.password = password

        self.cnx = mysql.connector.connect(
            host="localhost",
            database=DB_NAME,
            user=self.user,
            password=self.password,
        )
        self.cursor = self.cnx.cursor()

    def extract_data(self, nb_page):
        """Extract data from API."""
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.payload = {
            "json": 1,
            "action": "process",
            "page_size": 1000,
            "page": nb_page,
        }
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        try:
            r = requests.get(self.url, headers=self.headers, params=self.payload)
            self.result = r.json()
            self.products = self.result["products"]
            return self.products
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def insert_data(self, data):
        """Insert data into DB."""
        for product in data:
            prod_name = product["product_name_fr"]
            prod_url = product["url"]
            prod_brand = product["brands"]
            prod_store = product["stores"]
            nutriscore = product["nutriscore_grade"]

            try:
                self.cursor.execute(
                    "INSERT IGNORE INTO nutriscore\
                        (type)\
                    VALUES (%s);",
                    (nutriscore,),
                )

                self.cursor.execute(
                    "SELECT id FROM nutriscore where type = (%s);",
                    (nutriscore,),
                )
                nutriscore_id = self.cursor.fetchone()[0]
                self.cursor.execute(
                    "INSERT IGNORE INTO products\
                        (name, url, brand, stores, nutriscore_id)\
                    VALUES (%s, %s, %s, %s, %s);",
                    (
                        prod_name,
                        prod_url,
                        prod_brand,
                        prod_store,
                        nutriscore_id,
                    ),
                )

                last_pid0 = self.cursor.lastrowid

                categories = product["categories"].split(",")

                for category in categories:
                    category = category.strip()
                    category = re.sub(r"\w{2}\:", "", category)
                    self.cursor.execute(
                        "INSERT IGNORE INTO categories (name)\
                            VALUES (%s);",
                        (category,),
                    )

                    last_cid = self.cursor.lastrowid

                    self.cursor.execute(
                        "INSERT IGNORE INTO categories_products\
                            (products_id, categories_id)  VALUES (%s, %s);",
                        (last_pid0, last_cid),
                    )

                self.cnx.commit()
            except mysql.connector.Error as err:
                print("Failed inserting into database: {}".format(err))
                exit(1)

        self.cnx.close()


class Cleaner:
    """Clean all data."""

    validators: List = []
    normalizers: List = []

    def is_valid(self, data):
        """Vérifie si la clé 'data' est présente et retourne 1 ou 0."""
        for validator in self.validators:
            if not validator(data):
                return False
        return True

    def normalize(self, data):
        """Docstr."""
        for normalizer in self.normalizers:
            data = normalizer(data)
        return data

    def clean(self, collection):
        """Ne retourne que les données à 1 par is_valid."""
        return [self.normalize(data) for data in collection if self.is_valid(data)]


def require_product_name_fr_not_empty(data):
    """Verify if product_name_fr is not empty."""
    return True if data.get("product_name_fr") else False


def require_stores_not_empty(data):
    """Verify if stores is not empty."""
    return True if data.get("stores") else False


def require_nutriscore_grade_not_empty(data):
    """Verify if nutriscore_grade is not empty."""
    return True if data.get("nutriscore_grade") else False


class OffCleaner(Cleaner):
    """State."""

    validators = [
        require_product_name_fr_not_empty,
        require_stores_not_empty,
        require_nutriscore_grade_not_empty,
    ]


if __name__ == "__main__":
    for page in range(1, 6):
        con = Downloader("offp5", "spoff")
        extracted = con.extract_data(page)
        cleaner = OffCleaner()
        cleaned = cleaner.clean(extracted)
        con.insert_data(cleaned)
