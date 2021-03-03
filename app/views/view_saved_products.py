#!/usr/bin/env python
"""ViewSavedProducts module."""
from colorama import init  # type: ignore
from termcolor import colored

from app.views.view import View
from app import settings as s

init(autoreset=True)


class ViewSavedProducts(View):
    """View Product class."""

    def __init__(self):
        super().__init__()

    def display_saved_products(self):
        """Display products saved as substitutes."""
        print(self.header())
        print(f"\n{self.saved_products}\n")

    def input_saved_products(self, substitutes):
        """Input the saved products ."""
        choice = "\n".join(
            [
                colored(self.justify(str(index), 1), "yellow") + ". " + item.name
                for index, item in enumerate(substitutes, 1)
            ]
        )
        print(choice)
        print(f"{s.CR}{self.footer}")
        if s.ERROR:
            print(self.msg_error)
        print(self.back, self.quit)
