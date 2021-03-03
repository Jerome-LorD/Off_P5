#!/usr/bin/env python
"""ViewProduct module."""
from colorama import init  # type: ignore
from termcolor import colored

from app.views.view import View
from app import settings as s

init(autoreset=True)


class ViewProduct(View):
    """View Product class."""

    def __init__(self):
        super().__init__()

    def display_products(self, products, max_pages, page):
        """Display the products."""
        print(self.header())
        print(f"\n{self.select_product} page {page} / {max_pages}\n\n{self.next_prev}")

    def input_products(self, products):
        """Input the products."""
        choice = "\n".join(
            [
                colored(self.justify(str(index), 1), "yellow") + ". " + item.name
                for index, item in enumerate(products, 1)
            ]
        )
        print(choice)
        print(f"{s.CR}{self.footer}")
        if s.ERROR:
            print(self.msg_error)
        print(self.back, self.quit)
