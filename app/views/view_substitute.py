#!/usr/bin/env python
"""ViewSubstitute module."""
from colorama import init  # type: ignore
from termcolor import colored

from app.views.view import View
from app import settings as s

init(autoreset=True)


class ViewSubstitute(View):
    """View substitute class."""

    def __init__(self):
        super().__init__()

    def display_details(self, substituted, substitute):
        """Display the saved products details."""
        print(self.header())
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

    def display_no_subsitute(self, product):
        """Display an alert message if no substitute."""
        print(self.header())
        print(
            f"\n{self.you_have_selected} {product.name},{self.nutriscore}\
 {product.nutriscore.capitalize()}"
        )
        print(f"\n{self.no_substitute}\n")
        print(f"{s.CR}{self.footer}")
        print(self.back, self.quit)
        if s.ERROR:
            print(self.msg_error)

    def input_save(self, couple):
        """Input the save message.

        if there are two products, a backup menu is offered,
        otherwise no backup menu is offered.
        """
        if couple:
            self.menu_choices[0] = s.SAVE_ITEM
        else:
            self.menu_choices[0] = s.OTHER_ITEM
        choice = "\n".join(
            [
                colored(self.justify(str(index), 1), "yellow") + ". " + item
                for index, item in enumerate(self.menu_choices, 1)
            ]
        )
        print(choice)
