#!/usr/bin/env python
"""Download, clean and inserts datas into db."""
import os
import re

import mysql.connector  # type: ignore
import requests
from dotenv import load_dotenv, find_dotenv  # type: ignore
from typing import List, Any

from app.settings import DB_NAME
from app.models.database import Database


load_dotenv(find_dotenv())

user = os.getenv("OFF_USER")
password = os.getenv("OFF_PASSWD")


class Downloader:
    """Download and extract."""

    def __init__(self, nb_page):
        """Init."""
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.payload = {
            "json": 1,
            "action": "process",
            "lang": "fr",
            "page_size": 1000,
            "page": nb_page,
        }
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

    def extract_data(self):
        """Extract data from API."""
        try:
            r = requests.get(self.url, headers=self.headers, params=self.payload)
            self.result = r.json()
            self.products = self.result["products"]
            return self.products
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


class Insert:
    """Fill the database."""

    def __init__(self):
        """Init."""
        self.db = Database(user, password, DB_NAME)

    def is_data_in_db(self):
        """Check if the database contains at least 3000 entries."""
        self.db.cursor.execute("SELECT COUNT(products.id) as tot_prods FROM products")
        if self.db.cursor.fetchone()[0] >= 3000:
            return True
        return False

    def insert_data(self, products_data):
        """Insert data into DB."""
        for product in products_data:
            if product:
                prod_name = product["product_name_fr"]
                prod_url = product["url"]
                prod_brand = product["brands"]
                prod_store = product["stores"]
                nutriscore = product["nutriscore_grade"]

                try:
                    self.db.cursor.execute(
                        "INSERT IGNORE INTO nutriscore\
                            (type)\
                        VALUES (%s);",
                        (nutriscore,),
                    )

                    self.db.cursor.execute(
                        "SELECT id FROM nutriscore where type = (%s);",
                        (nutriscore,),
                    )
                    nutriscore_id = self.db.cursor.fetchone()[0]
                    self.db.cursor.execute(
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

                    last_products_id = self.db.cursor.lastrowid
                    categories = product["categories"].split(",")

                    for category in categories:
                        category = category.strip()
                        self.db.cursor.execute(
                            "INSERT IGNORE INTO categories (name)\
                                VALUES (%s);",
                            (category,),
                        )

                        self.db.cursor.execute(
                            "SELECT id FROM categories\
                            WHERE name = (%s);",
                            (category,),
                        )
                        last_categories_id = self.db.cursor.fetchone()[0]

                        self.db.cursor.execute(
                            "INSERT IGNORE INTO categories_products\
                                (products_id, categories_id)  VALUES (%s, %s);",
                            (last_products_id, last_categories_id),
                        )
                    self.db.cnx.commit()
                except mysql.connector.Error as err:
                    print("Failed inserting into database: {}".format(err))
                    exit(1)

        self.db.cnx.close()


class Cleaner:
    """Clean all data."""

    validators: List[Any] = []
    normalizers: List[Any] = []

    def is_valid(self, data):
        """Verify if the key has a value."""
        for validator in self.validators:
            if not validator(data):
                return False
        return True

    def normalize(self, data):
        """Normalize some entries."""
        for normalizer in self.normalizers:
            data = normalizer(data)
        return data

    def clean(self, collection):
        """Return a data list if is_valid is True."""
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


def require_lang_equal_to_fr(data):
    """Verify if lang is equal to fr."""
    return True if data.get("lang") == "fr" else False


def require_categories_lc_equal_to_fr(data):
    """Verify if categories_lc is equal to fr."""
    return True if data.get("categories_lc") == "fr" else False


def require_categories_without_lot_of_dashes(data):
    """Ignore categories with lot of tirets."""
    item = re.search(r"(\w+\-){1,}", data.get("categories"))
    return False if item else True


def normalize_product_without_cariage_return(data):
    """Delete cariage return."""
    if "\n" in data.get("product_name_fr"):
        return data.update(
            product_name_fr=data.get("product_name_fr").replace("\n", " ")
        )
    return data


def normalize_categories_without_suffix_and_bad_datas(data):
    """Delete expr like -> en: and fr: with all that comes after."""
    if data:
        item = re.search(r"\,\s{0,}\w{2}:", data.get("categories"))
        if item:
            return data.update(categories=data.get("categories")[: item.start()])
        return data


class OffCleaner(Cleaner):
    """State."""

    validators = [
        require_product_name_fr_not_empty,
        require_stores_not_empty,
        require_nutriscore_grade_not_empty,
        require_lang_equal_to_fr,
        require_categories_lc_equal_to_fr,
        require_categories_without_lot_of_dashes,
    ]

    normalizers = [
        normalize_product_without_cariage_return,
        normalize_categories_without_suffix_and_bad_datas,
    ]
