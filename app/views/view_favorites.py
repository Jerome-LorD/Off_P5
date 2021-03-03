#!/usr/bin/env python
"""ViewFavorites module."""
from colorama import init  # type: ignore
from termcolor import colored

from app.views.view import View
from app import settings as s

init(autoreset=True)


class ViewFavorites(View):
    """View Product class."""

    def __init__(self):
        """Init."""
        super().__init__()

    def display_favorites(self, substituted, substitute):
        """Display the saved products as favorites."""
        print(self.header())
        print(f"\n{self.saved_products}\n")
        print(f"\n{self.substituted_detail} :\n")
        for item in [substituted]:
            print(
                f"{self.product} : {item.name}\
\n{self.brand} : {item.brand.replace(',', ', ')}\
\n{self.stores} : {item.stores.replace(',', ', ')}\
\n{self.url} : {item.url}\
\n{self.nutriscore.capitalize()} : {item.nutriscore.capitalize()}"
            )
        print(f"\n{self.substitute_detail} :\n")
        for item in [substitute]:
            print(
                f"{self.product} : {item.name}\
\n{self.brand} : {item.brand.replace(',', ', ')}\
\n{self.stores} : {item.stores.replace(',', ', ')}\
\n{self.url} : {item.url}\
\n{self.nutriscore.capitalize()} : {item.nutriscore.capitalize()}"
            )
        print(f"{s.CR}{self.footer}")
        print(self.back, self.quit)
        if s.ERROR:
            print(self.msg_error)

    def input_menu_best_product(self):
        """Input the saved products details."""
        self.menu_choices[0] = s.DELETE_ITEM
        choice = "\n".join(
            [
                f"{colored(index, 'yellow')}. {item}"
                for index, item in enumerate(self.menu_choices, 1)
            ]
        )
        print(choice)
