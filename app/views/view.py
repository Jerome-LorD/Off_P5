#!/usr/bin/env python
"""Main page view."""
from colorama import init
from termcolor import colored

from app import settings as s

from app.models.category import Category
from app.models.product import Product

init(autoreset=True)


class View:
    """Main page."""

    def __init__(self):
        """Init."""
        self.category: Category = Category()
        self.product: Product = Product()
        self.commands = ""

    def header(self):
        """Display the header."""
        return f"\n{s.DASHES}\n{s.HEADER}\n{s.DASHES}"

    def display_categories(self, categories):
        """Display the categories."""
        print(self.header())
        print("\nSelectionnez une catégorie :\n")
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_products(self, products, max_pages, page):
        """Display the products."""
        print(self.header())
        print(
            f"\nSélectionnez un produit : page {page} / {max_pages}\n\
{colored('n', 'yellow')} : Page suivante\n{colored('p', 'yellow')} : Page précédente\n"
        )
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_detail_tst(self, instance):
        """Display the products details."""
        print("\nDétail du produit sélectionné :\n")
        print(
            f"Produit : {instance.name}\nMarque : {instance.brand}\nMagasin :\
 {instance.stores}\nURL : {instance.url}\nNutriscore :\
 {instance.nutriscore.capitalize()}"
        )

    def display_subsitute(self, details):
        """Display the substitute."""
        print("\nDétail du produit de substitution :\n")
        print(
            f"Produit : {details.name}\nMarque : {details.brand}\nMagasin :\
 {details.stores}\nURL : {details.url}\nNutriscore : \
 {details.nutriscore.capitalize()}\n"
        )
        print(s.SUB_HEADER)
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_no_subsitute(self):
        """Display the substitute."""
        print(
            "\nIl n'y à pas de produit avec un meilleur\
 nutriscore dans cette catégorie.\n"
        )
        print(s.SUB_HEADER)
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_no_subsitute_confirmed(self, instance):
        """Display the substitute."""
        print("\nDétail du produit sélectionné :\n")
        print(
            f"Produit : {instance.name}\nMarque : {instance.brand}\nMagasin :\
 {instance.stores}\nURL : {instance.url}\nNutriscore :\
 {instance.nutriscore.capitalize()}"
        )
        print("\nCe produit à le meilleur nutriscore dans sa catégorie.\n")
        print(s.SUB_HEADER)
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_no_better_nutriscore(self):
        """Display the substitute."""
        print("\nVotre choix est très bon, le nutriscore est le meilleur possible.\n")
        print(s.SUB_HEADER)
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_save_substitute(self):
        """Display the substitute."""
        print("\nLe produit à bien été enregistré dans votre liste.\n")
        print(s.SUB_HEADER)
        print(s.BACK_OR_QUIT)
        if s.ERROR:
            print(s.MSG_ERROR)

    def display_saved_products(self, substitutes):
        """Display the saved products as substitutes."""
        print("\nLes substituts que vous avez sélectionné :\n")

    def input_message(self, list_chosen):
        """Input the message."""
        choice = "\n".join(
            [
                colored(f"{nb}", "yellow") + f". {item.name} "
                for nb, item in enumerate(list_chosen, 1)
            ]
        )
        print(choice)

    def input_message_categories(self):
        """Input the message."""
        choice = "\n".join(
            [
                colored(f"{nb}", "yellow") + f". {item.name} "
                for nb, item in enumerate(self.categories, 1)
            ]
        )
        print(choice)

    def input_message_products(self):
        """Input the message."""
        choice = "\n".join(
            [
                colored(f"{nb}", "yellow") + f". {item.name} "
                for nb, item in enumerate(self.products, 1)
            ]
        )
        print(choice)

    def input_save(self):
        """Input the message."""
        choice = "\n".join(
            [
                colored(f"{nb}", "yellow") + f". {item} "
                for nb, item in s.MSG_SAVE.items()
            ]
        )
        print(choice)

    def input_saved(self):
        """Input the message."""
        choice = "\n".join(
            [
                colored(f"{nb}", "yellow") + f". {item} "
                for nb, item in s.MSG_SAVED.items()
            ]
        )
        print(choice)

    def input_saved_products(self, substitutes):
        """Input the message."""
        choice = "\n".join(
            [
                colored(f"{nb}", "yellow") + f". {item}"
                for nb, item in enumerate(substitutes, 1)
            ]
        )
        print(choice)

    def input_best_product(self):
        """Input the message."""
        choice = "\n".join(
            [
                colored(f"{nb}", "yellow") + f". {item} "
                for nb, item in s.MENU_CHOICES.items()
            ]
        )
        print(choice)
