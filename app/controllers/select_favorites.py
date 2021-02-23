#!/usr/bin/env python
"""SubstituteAlreadyInDb module."""
from app import settings as s
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
        self.indexes = [str(index) for index in range(1, len(s.MENU_CHOICES) + 1)]
        self.possible_commands = ["back-to-menu", s.QUIT_APP]  # settings

    def display(self):
        """Display."""
        return self.view.display_no_subsitute_confirmed(instance=self.instance)

    def get_input(self):
        """Get the input."""
        choice = self.view.input_best_product()
        choice = input(s.MSG_CHOICE)
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str):
        """Update."""
        if command in self.indexes:
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
