#!/usr/bin/env python
"""App file with Application class."""

from typing import Dict

from app.settings import QUIT_APP

from app.controllers.select_menu import SelectMenu
from app.controllers.select_category import SelectCategory
from app.controllers.select_product import SelectProduct
from app.controllers.select_detail import SelectDetail
from app.controllers.select_detail_tst import SelectDetailTst
from app.controllers.select_substitute import SelectSubstitute
from app.controllers.select_saved_products import SelectSavedProducts
from app.controllers.save_substitute import SaveSubstitute
from app.controllers.select_best_product import SelectBestProduct

from app.models.product import Product
from app.views.main_page import View


class Application:
    """Pur Beurre app class.

    1 - Quel aliment souhaitez-vous remplacer ?
    2 - Retrouver mes aliments substitués.

    L'utilisateur sélectionne 1. Le programme pose les questions suivantes à
    l'utilisateur et ce dernier sélectionne les réponses :

    Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre.
    L'utilisateur entre le chiffre correspondant et appuie sur entrée]
    Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre.
    L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée
    Le programme propose un substitut, sa description, un magasin ou l'acheter
    (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
    L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base
    de données.
    """

    Controllers: Dict[int, object] = {1: SelectCategory, 2: SelectSavedProducts}

    def __init__(self):
        """Init."""
        self.controller = SelectMenu()
        self.view = View()
        self.product: Product = Product()
        self.select_detail = SelectDetail(product_id=None, category_id=None)
        # self.select_detail_tst = SelectDetailTst(instance=())
        self.walk = True
        self.category_id: int = None
        self.product_id: int = None

    def run(self):
        """Run main method."""
        while self.walk:
            self.controller.display()
            command = self.controller.get_input()
            command = self.controller.update(command)
            self.update(command)

    def update(self, command: str):
        """Update."""
        # breakpoint()
        if isinstance(command, str) and command.startswith("select-menu-"):
            command = command[-1]
            controller = [
                instance
                for index, instance in self.Controllers.items()
                if index == int(command)
            ][0]
            self.controller = controller()

        if str(command).startswith("back-to-menu"):
            self.controller = SelectMenu()

        if str(command).startswith("select-category-"):
            self.category_id = int(command.replace("select-category-", ""))
            self.controller = SelectProduct(category_id=self.category_id)

        # if command == "already":
        #     self.controller = SubstituteAlreadyInDb()

        if command == "save":
            self.controller = SaveSubstitute()

        if isinstance(command, tuple):
            if command[1].startswith("best-product"):
                self.controller = SelectBestProduct(instance=command)
            if command[1].startswith("product"):
                self.controller = SelectDetailTst(instance=command)
            if command[1].startswith("substitute"):
                self.controller = SelectSubstitute(instance=command)

        if command == QUIT_APP:
            self.walk = False
