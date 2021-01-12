#!/usr/bin/env python
"""Tests."""
import requests
import logging
import mysql.connector
import re


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def insert_prods():
    """Insert in db."""
    for nb_page in range(1, 5):
        page_size = 1000
        url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        payload = {
            "json": 1,
            "action": "process",
            "page_size": page_size,
            "page": nb_page,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}

        r = requests.get(url, headers=headers, params=payload)
        res = r.json()

        cnx = mysql.connector.connect(
            host="localhost",
            user="offp5",
            database="offdb",
            password="spoff",
            charset="utf8",
        )

        cursor = cnx.cursor()

        products = res["products"]

        for product in products:
            if (
                "nutriscore_grade" in product
                and "product_name_fr" in product
                and "stores" in product
                and product["lang"] == "fr"
            ):

                prod_name = product["product_name_fr"]
                prod_url = product["url"]
                prod_brand = product["brands"]
                prod_store = product["stores"]

                try:
                    nutriscore = product["nutriscore_grade"]
                    cursor.execute(
                        "INSERT IGNORE INTO nutriscore\
                            (type)\
                        VALUES (%s);",
                        (nutriscore,),
                    )
                    cursor.execute(
                        "SELECT n_score_id FROM nutriscore where type = (%s);",
                        (nutriscore,),
                    )
                    nutriscore_id = cursor.fetchone()[0]
                    cursor.execute(
                        "INSERT IGNORE INTO products\
                            (product_name, url, brand, stores, nutriscore_id)\
                        VALUES (%s, %s, %s, %s, %s);",
                        (
                            prod_name,
                            prod_url,
                            prod_brand,
                            prod_store,
                            nutriscore_id,
                        ),
                    )

                    last_pid0 = cursor.lastrowid
                    # breakpoint()
                    # # logger.debug("last_pid0 : %s", last_pid0)
                    # sql = "INSERT IGNORE INTO substitutes (id) VALUES (%s);"
                    # cursor.execute(sql, last_pid0)

                    # last_pid1 = cursor.lastrowid

                    categories = product["categories"].split(",")

                    for category in categories:
                        category = category.strip()
                        category = re.sub(r"\w{2}\:", "", category)
                        cursor.execute(
                            "INSERT IGNORE INTO categories (category_name)\
                                VALUES (%s);",
                            (category.strip(),),
                        )

                        last_cid = cursor.lastrowid

                        cursor.execute(
                            "INSERT IGNORE INTO categories_products\
                                (products_id, categories_id)  VALUES (%s, %s);",
                            (last_pid0, last_cid),
                        )

                    cnx.commit()
                except mysql.connector.Error as err:
                    print("Failed inserting into database: {}".format(err))
                    exit(1)

        cnx.close()


if __name__ == "__main__":
    insert_prods()
