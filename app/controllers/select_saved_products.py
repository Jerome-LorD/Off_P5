#!/usr/bin/env python
"""Select saved products module."""
from app.settings import QUIT_APP, MSG_ERROR
from app.views.main_page import View
from app.models.product import Product


class SelectSavedProducts:
    """Select menu class."""

    def __init__(self):
        """Init."""
        self.view: View = View()
        self.product: Product = Product()
        self.substitutes = self.product.retrieve_substitute()
        self.indexes = [str(index) for index in range(1, len(self.substitutes) + 1)]
        self.possible_commands = ["back-to-menu", QUIT_APP]  # settings

    def display(self):
        """Display the saved products."""
        return self.view.display_saved_products(substitutes=self.substitutes)

    def get_input(self):
        """Get the input."""
        choice = input(self.view.input_saved_products(self.substitutes))
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return QUIT_APP
        return choice

    def update(self, command: str):
        """Update."""
        if command in self.indexes:
            instance = self.substitutes[int(command) - 1]
            product = Product().retrieve_substitute_from_pk(instance.nutriscore)
            return product, "best-product"

        elif command in self.possible_commands:
            if command == QUIT_APP:
                self.walk = False
            if command == "back-to-menu":
                return "back-to-menu"
        else:
            return MSG_ERROR
        return command
