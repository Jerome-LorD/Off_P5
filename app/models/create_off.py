#!/usr/bin/env python
"""Create database offdb."""
import mysql.connector  # type: ignore

import os

from dotenv import load_dotenv, find_dotenv  # type: ignore

from app.models.database import Database

from app.settings import SQL_FILE

load_dotenv(find_dotenv())
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWD")
user = os.getenv("OFF_USER")
password = os.getenv("OFF_PASSWD")


class Create:
    """Create db, user and tables."""

    def __init__(self):
        """Init."""
        self.db = Database(db_user, db_password)

    def create_user(self):
        """Create user."""
        try:
            self.db.cursor.execute(
                "CREATE USER IF NOT EXISTS %s@'localhost'\
                    IDENTIFIED WITH mysql_native_password BY %s;",
                (
                    user,
                    password,
                ),
            )
            self.db.cursor.execute(
                "GRANT ALL PRIVILEGES ON offdb.* TO %s@localhost WITH GRANT OPTION;",
                (user,),
            )
            self.db.cursor.execute("FLUSH PRIVILEGES;")

            self.db.cnx.commit()

        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")
            exit(1)

    def create_db(self):
        """Create db and tables."""
        try:
            with open(SQL_FILE) as f:
                for line in self.db.cursor.execute(f.read(), multi=True):
                    if line.with_rows:
                        line.fetchall()
        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")
            exit(1)

        self.db.cnx.close()


if __name__ == "__main__":
    conn = Create()
    conn.create_user()
    conn.create_db()
