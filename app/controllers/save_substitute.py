#!/usr/bin/env python
"""Select saved products module."""
from app.settings import MSG_ERROR, QUIT_APP
from app.views.main_page import View
from app.models.product import Product


class SaveSubstitute:
    """Save substitute."""

    def __init__(self):
        """Init."""
        self.view: View = View()
        self.product: Product = Product()
        self.substitutes = self.product.retrieve_substitute()
        self.indexes = [str(index) for index in range(1, len(self.substitutes) + 1)]
        self.possible_commands = ["back-to-menu", QUIT_APP]  # settings

    def display(self):
        """Display the menu."""
        return self.view.display_save_substitute()

    def get_input(self):
        """Get the input."""
        choice = input(self.view.input_save())
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return QUIT_APP
        return choice

    def update(self, command: str):
        """Select menu."""
        if command in self.indexes:
            if command == "save-in":
                return "save"
            if command == "go-menu":
                return "menu"

        elif command in self.possible_commands:
            if command == QUIT_APP:
                self.walk = False
            if command == "back-to-menu":
                return "back-to-menu"
        else:
            return MSG_ERROR
        return command
