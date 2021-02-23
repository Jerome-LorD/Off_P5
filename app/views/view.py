#!/usr/bin/env python
"""View module."""
import os

from colorama import init
from termcolor import colored

from app import settings as s

from app.models.category import Category
from app.models.product import Product

init(autoreset=True)


class View:
    """View class."""

    def __init__(self):
        """Init."""
        self.category: Category = Category()
        self.product: Product = Product()

    def clear(self):
        """Clear the terminal."""
        os.system("cls" if os.name == "nt" else "clear")

    def justify(self, text="", lenght: int = 0):
        """Justify the text."""
        return "{:>{}}".format(text, (len(text) + lenght))

    def header(self):
        """Display the header."""
        self.clear()
        return f"\n{s.DASHES}\n{s.HEADER}\n{s.DASHES}"

    def display_main_menu(self):
        """Display the main menu."""
        print(self.header())

    def display_categories(self):
        """Display the categories."""
        print(self.header())
        print(f"\n{s.SELECT_CATEGORY}\n")

    def display_products(self, products, max_pages, page):
        """Display the products."""
        print(self.header())
        print(
            f"\n{s.SELECT_PRODUCT} page {page} / {max_pages}\n\n{s.NEXT_PREVIOUS_PAGE}"
        )

    def display_details(self, substituted, substitute):
        """Display the saved products details."""
        print(self.header())
        print(f"\n{s.SUBSTITUTED_DETAIL} :\n")
        for item in [substituted]:
            print(
                f"{s.PRODUCT} : {item.name}\
\n{s.BRAND} : {item.brand.replace(',', ', ')}\
\n{s.STORES} : {item.stores.replace(',', ', ')}\
\n{s.URL} : {item.url}\
\n{s.NUTRISCORE.capitalize()} : {item.nutriscore.capitalize()}"
            )
        print(f"\n{s.SUBSTITUTE_DETAIL} :\n")
        for item in [substitute]:
            print(
                f"{s.PRODUCT} : {item.name}\
\n{s.BRAND} : {item.brand.replace(',', ', ')}\
\n{s.STORES} : {item.stores.replace(',', ', ')}\
\n{s.URL} : {item.url}\
\n{s.NUTRISCORE.capitalize()} : {item.nutriscore.capitalize()}"
            )
        print(f"{s.CR}{s.SUB_HEADER}")
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_favorites(self, substituted, substitute):
        """Display the saved products."""
        print(self.header())
        print(f"\n{s.SAVED_PRODUCTS}\n")
        print(f"\n{s.SUBSTITUTED_DETAIL} :\n")
        for item in [substituted]:
            print(
                f"{s.PRODUCT} : {item.name}\
\n{s.BRAND} : {item.brand.replace(',', ', ')}\
\n{s.STORES} : {item.stores.replace(',', ', ')}\
\n{s.URL} : {item.url}\
\n{s.NUTRISCORE.capitalize()} : {item.nutriscore.capitalize()}"
            )
        print(f"\n{s.SUBSTITUTE_DETAIL} :\n")
        for item in [substitute]:
            print(
                f"{s.PRODUCT} : {item.name}\
\n{s.BRAND} : {item.brand.replace(',', ', ')}\
\n{s.STORES} : {item.stores.replace(',', ', ')}\
\n{s.URL} : {item.url}\
\n{s.NUTRISCORE.capitalize()} : {item.nutriscore.capitalize()}"
            )
        print(f"{s.CR}{s.SUB_HEADER}")
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_no_subsitute(self, product):
        """Display an alert message.

        If there is no substitute because nutriscore is worse than A.
        """
        print(self.header())
        print(
            f"\n{s.YOU_HAVE_SELECTED} {product.name},{s.NUTRISCORE}\
 {product.nutriscore.capitalize()}"
        )
        print(f"\n{s.NO_SUBSTITUTE}\n")
        print(f"{s.CR}{s.SUB_HEADER}")
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_no_better_nutriscore(self, product):
        """Display an alert message if no substitute since the nutriscore is A."""
        print(self.header())
        print(
            f"\n{s.YOU_HAVE_SELECTED} : {product.name},{s.NUTRISCORE}\
 {product.nutriscore.capitalize()}"
        )
        print(f"\n{s.BEST_CHOICE}\n")
        print(f"{s.CR}{s.SUB_HEADER}")
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_save_substitute(self):
        """Display confirmation of saving substitute."""
        print(self.header())
        print(f"\n{s.CONFIRM_TITLE}\n")
        print(f"\n{s.CONFIRMATION}\n")
        print(f"{s.CR}{s.SUB_HEADER}")
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_saved_products(self):
        """Display products saved as substitutes."""
        print(self.header())
        print(f"\n{s.SAVED_PRODUCTS}\n")

    def input_message_menu(self):
        """Input the menu message."""
        print()
        choice = "\n".join(
            [
                colored(str(index), "yellow") + ". " + item
                for index, item in s.MENU_CHOICES.items()
            ]
        )
        print(choice)
        print(f"{s.CR}{s.SUB_HEADER}")
        if s.ERROR:
            print(s.MSG_ERROR)
        print(s.BACK_OR_QUIT)

    def input_categories(self, categories):
        """Input the categories."""
        choice = "\n".join(
            [
                colored(self.justify(str(index), 1), "yellow") + ". " + item.name
                for index, item in enumerate(categories, 1)
            ]
        )
        print(choice)
        print(f"{s.CR}{s.SUB_HEADER}")
        if s.ERROR:
            print(s.MSG_ERROR)
        print(s.BACK_OR_QUIT)

    def input_products(self, products):
        """Input the products."""
        choice = "\n".join(
            [
                colored(self.justify(str(index), 1), "yellow") + ". " + item.name
                for index, item in enumerate(products, 1)
            ]
        )
        print(choice)
        print(f"{s.CR}{s.SUB_HEADER}")
        if s.ERROR:
            print(s.MSG_ERROR)
        print(s.BACK_OR_QUIT)

    def input_save(self):
        """Input the save message."""
        choice = "\n".join(
            [
                colored(str(index), "yellow") + ". " + item
                for index, item in s.MSG_SAVE.items()
            ]
        )
        print(choice)

    def input_saved(self):
        """Input the saved message."""
        choice = "\n".join(
            [
                colored(str(index), "yellow") + ". " + item
                for index, item in s.MSG_SAVED.items()
            ]
        )
        print(choice)

    def input_saved_products(self, substitutes):
        """Input the saved products ."""
        choice = "\n".join(
            [
                colored(self.justify(str(index), 1), "yellow") + ". " + item.name
                for index, item in enumerate(substitutes, 1)
            ]
        )
        print(choice)
        print(f"{s.CR}{s.SUB_HEADER}")
        if s.ERROR:
            print(s.MSG_ERROR)
        print(s.BACK_OR_QUIT)

    def input_menu_best_product(self):
        """Input the saved products details."""
        choice = "\n".join(
            [
                colored(index, "yellow") + ". " + item
                for index, item in s.MENU_CHOICES.items()
            ]
        )
        print(choice)
