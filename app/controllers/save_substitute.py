#!/usr/bin/env python
"""Select saved products module."""
from app import settings as s
from app.views.view import View
from app.models.product import Product


class SaveSubstitute:
    """Save substitute."""

    def __init__(self):
        """Init."""
        self.view: View = View()
        self.product: Product = Product()
        self.substitutes = self.product.retrieve_substitute()
        self.indexes = [str(index) for index in range(1, len(self.substitutes) + 1)]
        self.possible_commands = ["back-to-menu", s.QUIT_APP]

    def display(self):
        """Display the menu."""
        return self.view.display_save_substitute()

    def get_input(self):
        """Get the input."""
        choice = self.view.input_saved()
        choice = input(s.MSG_CHOICE)
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str) -> str:
        """Select menu."""
        if command in self.indexes:
            if command == "1":
                return f"select-menu-{command}"
            if command == "2":
                return f"select-menu-{command}"

        elif command in self.possible_commands:
            if command == s.QUIT_APP:
                self.walk = False
            if command == "back-to-menu":
                return "back-to-menu"
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command
