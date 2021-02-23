#!/usr/bin/env python
"""SubstituteAlreadyInDb module."""
from app import settings as s
from app.views.view import View
from app.models.product import Product


class SelectFavorites:
    """SelectBestProduct class."""

    def __init__(self, substitute_id, substituted_id):
        """Init."""
        self.view: View = View()
        self.product: Product = Product()
        self.substituted_id = substituted_id
        self.substitute_id = substitute_id
        self.substitute = self.product.retrieve_substitute_from_pk(
            pk=self.substitute_id
        )
        self.substituted = self.product.retrieve(self.substituted_id)
        self.indexes = [str(index) for index in range(1, len(s.MENU_CHOICES) + 1)]
        self.possible_commands = ["back-to-menu", s.QUIT_APP]

    def display(self):
        """Display."""
        return self.view.display_favorites(self.substituted[0], self.substitute)

    def get_input(self) -> str:
        """Get the input."""
        choice = self.view.input_menu_best_product()
        choice = input(s.MSG_CHOICE)
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str) -> str:
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
