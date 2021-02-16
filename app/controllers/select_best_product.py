#!/usr/bin/env python
"""SubstituteAlreadyInDb module."""
from app.settings import QUIT_APP, MSG_ERROR, MENU_CHOICES
from app.views.main_page import View
from app.models.product import Product


class SelectBestProduct:
    """SelectBestProduct class."""

    def __init__(self, instance):
        """Init."""
        self.view: View = View()
        self.product: Product = Product()
        self.instance = instance[0]
        self.substitute = self.product.find_substitute(
            selected_product=self.instance.pk
        )
        self.indexes = [str(index) for index in range(1, len(MENU_CHOICES) + 1)]
        self.possible_commands = ["back-to-menu", QUIT_APP]  # settings

    def display(self):
        """Display."""
        return self.view.display_no_subsitute_confirmed(instance=self.instance)

    def get_input(self):
        """Get the input.

        Renvoi un input qui donne ce choix :
        Chercher un autre produit sauvegardé
        Faire une nouvelle recherche d'aliment à remplacer
        """
        choice = input(self.view.input_best_product())
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return QUIT_APP
        return choice

    def update(self, command: str):
        """Update."""
        if command in self.indexes:
            return f"select-menu-{command}"
        elif command in self.possible_commands:
            if command == QUIT_APP:
                self.walk = False
            if command == "back-to-menu":
                return "back-to-menu"
        else:
            return MSG_ERROR
        return command
