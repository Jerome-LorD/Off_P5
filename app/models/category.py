#!/usr/bin/env python
"""Category file."""
import os

from dotenv import load_dotenv, find_dotenv

from app.models.database import Database


load_dotenv(find_dotenv())


off_user = os.getenv("OFF_USER")
off_password = os.getenv("OFF_PASSWD")
off_database = os.getenv("OFF_DB")


class Category:
    """Category class."""

    def __init__(
        self,
        name: str = "",
        nutriscore: str = "",
        brand: str = "",
        stores: str = "",
        url: str = "",
        pk: int = None,
        best_category_id: int = None,
        total_produtcs_in_fewest_category: int = None,
    ):
        """Init."""
        self.name = name
        self.nutriscore = nutriscore
        self.brand = brand
        self.stores = stores
        self.url = url
        self.product_id = pk
        self.best_category_id = best_category_id
        self.total_produtcs_in_fewest_category = total_produtcs_in_fewest_category

        self.walk: bool = True

    def __str__(self):
        """Return name as default value."""
        return f"{self.name}"

    def __repr__(self):
        """Return Format str."""
        return f"{self.name} - {self.nutriscore} - {self.brand} - {self.stores}\
 - {self.url} - {self.product_id} - {self.best_category_id} -\
 {self.total_produtcs_in_fewest_category}"

    @classmethod
    def retrieve(cls):
        """Select 30 categories."""
        cls.db = Database(off_user, off_password, off_database)
        cls.db.cursor.execute(
            "SELECT categories.name, categories.id, COUNT(products.id) as total_products\
                        FROM categories_products\
                        INNER JOIN products\
                        ON categories_products.products_id = products.id\
                        JOIN categories\
                        ON categories.id = categories_products.categories_id\
                        GROUP BY categories.name\
                        ORDER BY total_products  DESC LIMIT 30"
        )

        return [Category(name=line[0], pk=line[1]) for line in cls.db.cursor.fetchall()]

    @classmethod
    def find_best_category(cls, pk, offset):
        """Find the best category."""
        cls.db = Database(off_user, off_password, off_database)
        cls.db.cursor.execute(
            "SELECT p.name, ns.type, p.brand, p.stores, p.url, p.id,\
                             c.id as category_with_the_fewest_products, (\
                        SELECT COUNT(p_in.id) tot_in\
                        FROM products p_in\
                        JOIN categories_products cp_in\
                        ON p_in.id = cp_in.products_id\
                        JOIN categories c_in\
                        ON c_in.id = cp_in.categories_id\
                        where c_in.id in (category_with_the_fewest_products) \
                        GROUP BY c_in.name\
                    ) as tot_produtcs_in_fewest_category\
            FROM products p\
            JOIN categories_products cp\
            ON cp.products_id = p.id\
            JOIN categories c\
            ON cp.categories_id = c.id\
            JOIN nutriscore ns\
            ON p.nutriscore_id = ns.id\
            WHERE p.id = %s\
            GROUP BY tot_produtcs_in_fewest_category\
            ORDER BY tot_produtcs_in_fewest_category ASC LIMIT 1 OFFSET %s",
            (
                pk,
                offset,
            ),
        )
        return [Category(*line) for line in cls.db.cursor.fetchall()]
