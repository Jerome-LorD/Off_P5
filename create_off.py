#!/usr/bin/env python
"""Create database offdb."""
import mysql.connector

import os

from dotenv import load_dotenv, find_dotenv

from settings import SQL_FILE

load_dotenv(find_dotenv())
dbpass = os.getenv("DB_PASSWD")


class Create:
    """Create db, user and tables."""

    def __init__(self):
        """Init."""
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password=dbpass,
        )

        self.cursor = self.cnx.cursor()

    def create_user(self, dbuser, dbpassword):
        """Create user."""
        try:
            self.cursor.execute(
                "CREATE USER IF NOT EXISTS %s@'localhost'\
                    IDENTIFIED WITH mysql_native_password BY %s;",
                (
                    dbuser,
                    dbpassword,
                ),
            )
            self.cursor.execute(
                "GRANT ALL PRIVILEGES ON offdb.* TO %s@localhost WITH GRANT OPTION;",
                (dbuser,),
            )
            self.cursor.execute("FLUSH PRIVILEGES;")

            self.cnx.commit()

        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")
            exit(1)

    def create_db(self):
        """Create db and tables."""
        try:
            with open(SQL_FILE) as f:
                for line in self.cursor.execute(f.read(), multi=True):
                    if line.with_rows:
                        line.fetchall()
        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")
            exit(1)

        self.cnx.close()


if __name__ == "__main__":
    conn = Create()
    conn.create_user("offp5", "spoff")
    conn.create_db()
