#!/usr/bin/env python
"""Database cnx."""

import mysql.connector  # type: ignore
import os

from dotenv import load_dotenv, find_dotenv  # type: ignore

load_dotenv(find_dotenv())

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWD")
off_user = os.getenv("OFF_USER")
off_password = os.getenv("OFF_PASSWD")
off_database = os.getenv("OFF_DB")
host = os.getenv("DB_HOST")


class Database:
    """Database class."""

    cnx = None

    def __init__(self, user="", password="", schema=None):
        """Init."""
        self.user: str = user
        self.password: str = password
        self.schema: str = schema

        if not self.cnx:
            self.cnx = mysql.connector.connect(
                host=host,
                database=self.schema,
                user=self.user,
                password=self.password,
            )

        self.cursor = self.cnx.cursor()

    @classmethod
    def is_connected(cls):
        """Verify connexion."""
        return cls.cnx is not None
