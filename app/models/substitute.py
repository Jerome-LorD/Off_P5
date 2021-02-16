#!/usr/bin/env python
"""Substitute module."""
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


off_user = os.getenv("OFF_USER")
off_password = os.getenv("OFF_PASSWD")
off_database = os.getenv("OFF_DB")


class Substitute:
    """Substitute class."""

    def __init__(self, substituted_id: int = None, substitute_id: int = None):
        """Init."""
        self.substituted_id = substituted_id
        self.substitute_id = substitute_id


if __name__ == "__main__":
    pass
