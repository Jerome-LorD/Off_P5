#!/usr/bin/env python
"""Select saved products module."""
from app import settings as s
from app.views.view_saved_products import ViewSavedProducts
from app.models.product import Product


class SelectSavedProducts:
    """Select menu class."""

    def __init__(self):
        """Init."""
        self.view: ViewSavedProducts = ViewSavedProducts()
        self.product: Product = Product()
        self.substitutes = self.product.retrieve_substitute()
        self.indexes = [str(index) for index in range(1, len(self.substitutes) + 1)]
        self.possible_commands = ["back-to-menu", s.QUIT_APP]

    def display(self):
        """Display the saved products."""
        return self.view.display_saved_products()

    def get_input(self):
        """Get the input."""
        self.view.input_saved_products(substitutes=self.substitutes)
        choice = input(self.view.msg_choice)
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str) -> str:
        """Update the controller."""
        if command in self.indexes:
            substitute = self.substitutes[int(command) - 1]
            substituted = self.product.retrieve(substitute.substituted_id)
            substituted = substituted[0]
            return f"substitute-substituted-{substitute.pk}&{substituted.pk}"

        elif command in self.possible_commands:
            if command == s.QUIT_APP:
                self.walk = False
            if command == "back-to-menu":
                return "back-to-menu"
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command
