#!/usr/bin/env python
"""Category file."""
import os

from dotenv import load_dotenv, find_dotenv

from app.models.database import Database
from app.models.category import Category


load_dotenv(find_dotenv())


off_user = os.getenv("OFF_USER")
off_password = os.getenv("OFF_PASSWD")
off_database = os.getenv("OFF_DB")


class Product:
    """Product class."""

    def __init__(
        self,
        name: str = "",
        nutriscore: str = "",
        brand: str = "",
        stores: str = "",
        url: str = "",
        pk: int = None,
        substituted_id: int = None,
        substitutes_id: int = None,
    ):
        """Init."""
        self.name = name
        self.nutriscore = nutriscore
        self.brand = brand
        self.stores = stores
        self.url = url
        self.pk = pk
        self.substituted_id = substituted_id
        self.substitutes_id = substitutes_id

        self.page_index = 1
        self.limit = 30
        self.total_lines = 0

        self.db = Database(off_user, off_password, off_database)
        self.category: Category = Category()

    def __str__(self):
        """Return name as default value."""
        return f"{self.name}"

    def __repr__(self):
        """Return Format str."""
        return f"{self.name} - {self.nutriscore} - {self.brand} - {self.stores}\
 - {self.url} - {self.pk} - {self.substituted_id} - {self.substitutes_id}"

    @property
    def offset(self):
        """Return offset from page number."""
        return (self.page_index - 1) * self.limit

    def change_page(self):
        """Change page."""
        return self.page_index, self.max_pages

    @property
    def max_pages(self):
        """Define the nb of max pages."""
        return self.total_lines // self.limit

    @property
    def has_previous_page(self):
        """Check if the previous page exists."""
        if self.page_index > 1:
            return True
        return False

    @property
    def has_next_page(self):
        """Check if the next page exists."""
        if self.page_index < self.max_pages:
            return True
        return False

    def save_substitute(self, substituted_id, substitute_id):
        """Save Product into database."""
        self.db.cursor.execute(
            "SELECT s.substitute_id, s.substituted_id\
            FROM substitutes s\
            WHERE s.substitute_id = %s and s.substituted_id = %s",
            (
                substitute_id,
                substituted_id,
            ),
        )
        rows = self.db.cursor.fetchall()
        self.db.cursor.execute(
            "INSERT INTO substitutes\
                (substitute_id, substituted_id) VALUES (%s, %s)",
            (
                substitute_id,
                substituted_id,
            ),
        )
        if rows:
            if substitute_id not in rows[0] and substituted_id not in rows[0]:
                self.db.cnx.commit()
        else:
            self.db.cnx.commit()

    def delete_substitutes(self, substitutes_id):
        """Delete substitutes row."""
        self.db.cursor.execute(
            "DELETE FROM `substitutes` WHERE `substitutes`.`id` = %s",
            (substitutes_id,),
        )
        self.db.cnx.commit()

    def is_substitute_in_db(self, substitute_id):
        """Check if substitute already in db."""
        self.db.cursor.execute(
            "SELECT s.substitute_id\
        FROM substitutes s\
        JOIN products\
        ON products.id = s.substitute_id\
        WHERE s.substitute_id = %s",
            (substitute_id,),
        )
        if self.db.cursor.fetchall():
            return True
        else:
            return False

    def get_total_lines(self, pk):
        """Get total product per category."""
        self.db = Database(off_user, off_password, off_database)
        self.db.cursor.execute(
            "SELECT COUNT(products.id) as total_lines\
                FROM categories\
                JOIN categories_products\
                ON categories.id = categories_products.categories_id\
                JOIN products\
                ON categories_products.products_id = products.id\
                JOIN nutriscore\
                ON nutriscore.id = products.nutriscore_id\
                WHERE categories.id = %s",
            (pk,),
        )
        self.total_lines = self.db.cursor.fetchone()[0]
        return self.total_lines

    @classmethod
    def list(cls, pk, limit, offset):
        """List the products."""
        cls.db = Database(off_user, off_password, off_database)
        cls.db.cursor.execute(
            "SELECT p.name, ns.type, p.brand, p.stores, p.url, p.id\
                FROM categories c\
                JOIN categories_products cp\
                ON c.id = cp.categories_id\
                JOIN products p\
                ON cp.products_id = p.id\
                JOIN nutriscore ns\
                ON p.nutriscore_id = ns.id\
                WHERE c.id = %s LIMIT %s OFFSET %s",
            (pk, limit, offset),
        )
        return [Product(*line) for line in cls.db.cursor.fetchall()]

    @classmethod
    def retrieve(cls, pk: int):
        """Retrieve the products."""
        cls.db = Database(off_user, off_password, off_database)
        cls.db.cursor.execute(
            "SELECT p.name, ns.type, p.brand, p.stores, p.url, p.id\
                FROM products p\
                JOIN categories_products cp\
                ON p.id = cp.products_id\
                JOIN categories c\
                ON cp.categories_id = c.id\
                JOIN nutriscore ns\
                ON p.nutriscore_id = ns.id\
                WHERE p.id = (%s) LIMIT 1",
            (pk,),
        )
        return [Product(*line) for line in cls.db.cursor.fetchall()]

    def retrieve_substitute_from_pk(self, pk: int):
        """Retrieve the products."""
        self.db.cursor.execute(
            "SELECT p.name, ns.type, p.brand, p.stores, p.url, p.id, p.id, s.id\
                FROM substitutes s\
                JOIN products p\
                ON p.id = s.substitute_id\
                JOIN nutriscore ns\
                ON ns.id = p.nutriscore_id\
                WHERE s.substitute_id = (%s);",
            (pk,),
        )
        # breakpoint()
        res = [Product(*line) for line in self.db.cursor.fetchall()][0]

        return res

    @classmethod
    def retrieve_substitute(cls):
        """Retrieve the saved substitute."""
        cls.db = Database(off_user, off_password, off_database)
        cls.db.cursor.execute(
            "SELECT p.name, ns.type, p.brand, p.stores, p.url, p.id, substituted.id\
                FROM substitutes s\
                JOIN products substitute\
                ON s.substitute_id = substitute.id\
                JOIN products substituted\
                ON s.substituted_id = substituted.id\
                JOIN products p\
                ON p.id = substitute.id\
                JOIN nutriscore ns\
                ON ns.id = p.nutriscore_id",
        )
        return [Product(*line) for line in cls.db.cursor.fetchall()]

    @classmethod
    def find_substitute_from_category(cls, best_category_id):
        """Find substitute."""
        cls.db = Database(off_user, off_password, off_database)
        cls.db.cursor.execute(
            "SELECT products.name, nutriscore.type, products.brand, products.stores,\
        products.url, products.id\
        FROM products\
        JOIN nutriscore\
        ON nutriscore.id = products.nutriscore_id\
        JOIN categories_products\
        ON categories_products.products_id = products.id\
        JOIN categories\
        ON categories_products.categories_id = categories.id\
        WHERE categories.id = %s and nutriscore.type < (\
            SELECT GROUP_CONCAT(DISTINCT nutriscore.type SEPARATOR ', ') AS liste\
            FROM products\
            JOIN nutriscore\
            ON nutriscore.id = products.nutriscore_id\
            JOIN categories_products\
            ON categories_products.products_id = products.id\
            JOIN categories\
            ON categories_products.categories_id = categories.id\
            WHERE categories.id = %s  )\
            ORDER BY RAND() LIMIT 1",
            (
                best_category_id,
                best_category_id,
            ),
        )
        return [Product(*line) for line in cls.db.cursor.fetchall()]

    def find_substitute(self, selected_product):
        """Find substitutes."""
        substitute = None
        offset = 0

        while not substitute:
            substituted = Category().find_best_category(
                pk=selected_product, offset=offset
            )
            substituted = substituted[0]

            if not substituted:
                return None

            substitute = self.find_substitute_from_category(
                best_category_id=substituted.best_category_id
            )
            if substitute:
                return substitute[0]
            offset += 1

            offset_limit = 5
            if offset == offset_limit:
                return None
