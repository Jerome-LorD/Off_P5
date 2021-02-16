#!/usr/bin/env python
"""Select detail product module."""
from app.settings import QUIT_APP, MSG_SAVE, MSG_ERROR

from app.models.product import Product
from app.views.main_page import View


class SelectSubstitute:
    """Select substitute."""

    def __init__(self, instance):
        """Init."""
        self.product: Product = Product()
        self.view: View = View()
        self.instance = instance[0]
        self.substitute = self.product.find_substitute(
            selected_product=self.instance.pk
        )

        self.indexes = [str(index) for index in range(1, len(MSG_SAVE) + 1)]
        """Ici possible de checker si le substitut est déja en db"""
        # if self.product.is_substitute_in_db(self.substitute.pk):
        #     MSG_SAVE = [
        #         item.replace(
        #             "Sauvegarder le substitut",
        #             "Consulter la liste des produits enregistrés",
        #         )
        #         for item in MSG_SAVE
        #     ]
        self.possible_commands = ["next-page", "previous-page", QUIT_APP]  # settings

    def display(self):
        """Display the substitute."""
        if self.instance.nutriscore == "a":
            self.view.display_no_better_nutriscore()
        elif (
            self.instance.nutriscore != "a"
            and self.substitute.nutriscore == self.instance.nutriscore
        ):
            self.view.display_no_subsitute()
        else:
            self.view.display_subsitute(details=self.substitute)

    def get_input(self):
        """Get input."""
        # Si pas de nutriscore meilleur
        return input(self.view.input_save())

    def update(self, command: str):
        """Update the controller.

        Si le substitut est à proposer:
        1. Sauvegarder le substitut
        2. Revennir au menu principal

        si le substitut est déjà enregistré
        1. Consulter la liste des produits enregistrés
        1. Revennir au menu principal

        menu = {}
        """
        if command in self.indexes:
            # command = self.categories[int(command) - 1]
            if command == "1":
                if self.substitute:
                    if self.product.is_substitute_in_db(self.substitute.pk):
                        return "already"
                    else:
                        self.product.save_substitute(
                            self.instance.pk, self.substitute.pk
                        )
                        return "save"
                else:
                    self.product.save_substitute(self.instance.pk, self.instance.pk)
                    return "save"
            if command == "2":
                return "menu"

        elif command == QUIT_APP:
            self.walk = False
        else:
            return MSG_ERROR
        return command
