#!/usr/bin/env python
"""Main page view."""
# from termcolor import colored

from app.settings import HEADER, DASHES, MSG_SAVE, MSG_BEST_PRODUCTS, MENU_CHOICES

from app.models.category import Category
from app.models.product import Product

# from app.controllers.select_category import SelectCategory

# from app.controllers.select_product import SelectProduct


class View:
    """Main page."""

    def __init__(self):
        """Init."""
        self.category: Category = Category()
        self.product: Product = Product()
        self.commands = ""

    def header(self):
        """Display the header."""
        return f"\n{DASHES}\n{HEADER}\n{DASHES}"

    def display_categories(self, categories):
        """Display the categories."""
        print(self.header())
        print("\nSelectionnez une catégorie :\n")

    def display_products(self, products, max_pages, page):
        """Display the products."""
        print(self.header())
        print(f"\nSélectionnez un produit : page {page} / {max_pages}\n")

    #     def display_detail(self, details):
    #         """Display the products details."""
    #         print("\nDétail du produit sélectionné :\n")
    #         print(
    #             f"Produit :{details.name}\nMarque : {details.brand}\nMagasin :\
    # {details.stores}\nURL : {details.url}\nNutriscore : {details.nutriscore}"
    #         )

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
 {details.stores}\nURL : {details.url}\nNutriscore : {details.nutriscore.capitalize()}\n"
        )
        print("-------------- Voulez vous : --------------\n")
        # print("\n1. Sauvegarder le produit\n2. Revenir au menu principal\n")
        self.walk = False

    def display_no_subsitute(self):
        """Display the substitute."""
        print("\nNous n'avons pas trouvé de produit avec un meilleur nutriscore.\n")
        print("-------------- Voulez vous : --------------\n")
        self.walk = False

    def display_no_subsitute_confirmed(self, instance):
        """Display the substitute."""
        print("\nDétail du produit sélectionné :\n")
        print(
            f"Produit : {instance.name}\nMarque : {instance.brand}\nMagasin :\
 {instance.stores}\nURL : {instance.url}\nNutriscore :\
 {instance.nutriscore.capitalize()}"
        )
        print("\nCe produit à le meilleur nutriscore dans sa catégorie.\n")
        print("-------------- Voulez vous : --------------\n")

    def display_no_better_nutriscore(self):
        """Display the substitute."""
        print("\nVotre choix est très bon, le nutriscore est le meilleur possible.\n")
        print("-------------- Voulez vous : --------------\n")
        self.walk = False

    def display_save_substitute(self):
        """Display the substitute."""
        print("\nLe produit à bien été enregistré dans votre liste.\n")
        print("-------------- Voulez vous : --------------\n")

    def display_saved_products(self, substitutes):
        """Display the saved products as substitutes."""
        print("\nListe des substituts que vous avez sélectionné :\n")
        # print(
        #     "\n".join(
        #         [
        #             f"{index}. {substitute}"
        #             for index, substitute in enumerate(substitutes, 1)
        #         ]
        #     )
        # )

        # print("\nCréer un input ici pour sélectionner un produits.\n")
        # self.walk = False

    def input_message(self, list_chosen):
        """Input the message."""
        return "\n".join(
            [f"{nb}. {item.name} " for nb, item in enumerate(list_chosen, 1)]
        )

    def input_message_categories(self):
        """Input the message."""
        return "\n".join(
            [f"{nb}. {item.name} " for nb, item in enumerate(self.categories, 1)]
        )

    def input_message_products(self):
        """Input the message."""
        return "\n".join(
            [f"{nb}. {item.name} " for nb, item in enumerate(self.products, 1)]
        )

    def input_save(self):
        """Input the message."""
        return "\n".join([f"{nb}. {item} " for nb, item in MSG_SAVE.items()])

    def input_saved_products(self, substitutes):
        """Input the message."""
        return "\n".join([f"{nb}. {item} " for nb, item in enumerate(substitutes, 1)])
        # return "\n".join([f"{nb}. {item} " for nb, item in MSG_SAVE.items()])

    def input_best_product(self):
        """Input the message."""
        return "\n".join([f"{nb}. {item} " for nb, item in MENU_CHOICES.items()])
