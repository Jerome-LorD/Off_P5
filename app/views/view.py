#!/usr/bin/env python
"""View module."""
import os

from colorama import init  # type: ignore
from termcolor import colored

from app import settings as s

from app.models.category import Category
from app.models.product import Product

init(autoreset=True)


class View:
    """View class."""

    ANSI_LEN = len(colored("", "blue", attrs=["bold"]))

    def __init__(self):
        """Init."""
        self.category: Category = Category()
        self.product: Product = Product()

        self.del_substitute = True

        self.menu_choices = [
            "Rechercher un aliment à remplacer",
            "Retrouver mes aliments substitués.",
        ]

        self.back = f'{colored(self.justify("m", 1), "yellow")} : {s.BACK}'
        self.quit = f'\n{colored(self.justify("q", 1), "yellow")} : {s.QUIT}\n'
        self.msg_choice = f"\n\n{self.justify(s.MSG_CHOICE, 3)}"
        self.select_category = colored(self.justify(s.SELECT_CATEGORY, 2), "cyan")
        self.select_product = colored(self.justify(s.SELECT_PRODUCT, 2), "cyan")

        self.product = self.justify(s.PRODUCT, 1)
        self.brand = self.justify(s.BRAND, 1)
        self.stores = self.justify(s.STORES, 1)
        self.url = self.justify(s.URL, 1)
        self.nutriscore = self.justify(s.NUTRISCORE, 1)

        self.msg_error = colored(self.justify(s.MSG_ERROR, 3), "red")
        self.no_substitute = colored(self.justify(s.NO_SUBSTITUTE, 3), "red")
        self.save_confirm = colored(self.justify(s.SAVE_CONFIRM, 3), "green")
        self.saved_products = self.justify(s.SAVED_PRODUCTS, 2)
        self.substituted_detail = colored(self.justify(s.SUBSTITUTED_DETAIL, 2), "cyan")
        self.substitute_detail = colored(self.justify(s.SUBSTITUTE_DETAIL, 2), "cyan")
        self.confirm_title = self.justify(s.CONFIRM_TITLE, 3)
        self.you_have_selected = colored(self.justify(s.YOU_HAVE_SELECTED, 3), "cyan")
        self.del_alert = self.justify(colored(s.DEL_ALERT, "red"), 3)
        self.othr_cmd = self.centerize(s.OTHER_COMMANDS, s.CHAR_LENGHT)
        self.app_title = self.centerize(s.APP_TITLE, s.CHAR_LENGHT)
        self.head = self.justify(
            f"{s.DSH * 6}{colored(self.app_title, 'blue', attrs=['bold'])}{s.DSH * 6}",
            1,
        )
        self.dashes = self.justify(s.DSH * (len(self.head) - self.ANSI_LEN - 1), 1)
        self.footer = self.justify(
            f"{s.DSH * 6}{colored(self.othr_cmd, 'blue', attrs=['bold'])}{s.DSH * 6}\n",
            1,
        )
        self.next_prev = f"{colored(self.justify('p', 1), 'yellow')} : Page précédente\
 | {colored('n', 'yellow')} : Page suivante\n"

    def clear(self):
        """Clear the terminal."""
        os.system("cls" if os.name == "nt" else "clear")

    def justify(self, text="", lenght: int = 0):
        """Justify the text."""
        return "{:>{}}".format(text, (len(text) + lenght))

    def centerize(self, text="", lenght: int = 0):
        """Centerize the text."""
        return "{: ^{}}".format(text, (len(text) + lenght))

    def header(self):
        """Display the header."""
        self.clear()
        return f"\n{self.dashes}\n{self.head}\n{self.dashes}"
