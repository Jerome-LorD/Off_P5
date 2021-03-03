#!/usr/bin/env python
"""SubstituteAlreadyInDb module."""
from app import settings as s
from app.views.view_favorites import ViewFavorites
from app.models.product import Product


class SelectFavorites:
    """SelectBestProduct class."""

    def __init__(self, substitute_id, substituted_id):
        """Init."""
        self.view: ViewFavorites = ViewFavorites()
        self.product: Product = Product()
        self.substituted_id = substituted_id
        self.substitute_id = substitute_id
        self.substitute = self.product.retrieve_substitute_from_pk(
            pk=self.substitute_id
        )
        self.substituted = self.product.retrieve(self.substituted_id)
        self.indexes = [
            str(index) for index in range(1, len(self.view.menu_choices) + 1)
        ]
        # breakpoint()
        self.possible_commands = ["del_favorite", "back-to-menu", s.QUIT_APP]

    def display(self):
        """Display."""
        return self.view.display_favorites(self.substituted[0], self.substitute)

    def get_input(self) -> str:
        """Get the input."""
        self.view.input_menu_best_product()
        choice = input(self.view.msg_choice)
        if choice == "1":
            return "del_favorite"
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str) -> str:
        """Update the controller."""
        if command in self.indexes:
            return f"select-menu-{command}"
        elif command in self.possible_commands:
            if command == "del_favorite":
                return f"delete-substituted_id-substitute_id-\
{self.substitute.substitutes_id}&{self.substituted_id}&{self.substitute_id}"

            if command == s.QUIT_APP:
                return s.QUIT_APP
            if command == "back-to-menu":
                return "back-to-menu"
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command
