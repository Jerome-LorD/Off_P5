#!/usr/bin/env python
"""Delete substitute module."""
from app import settings as s
from app.views.view_delete_substitutes import ViewDeleteSubstitutes
from app.models.product import Product


class DeleteSubstitutes:
    """Delete substitutes_id row in db."""

    def __init__(self, substitutes_id, substituted_id, substitute_id):
        """Init."""
        self.substitutes_id = substitutes_id
        self.substituted_id = substituted_id
        self.substitute_id = substitute_id
        self.view: ViewDeleteSubstitutes = ViewDeleteSubstitutes()
        self.product: Product = Product()
        self.substituted = self.product.retrieve(self.substituted_id)
        self.substituted = self.substituted[0]
        self.substitute = self.product.retrieve(self.substitute_id)
        self.substitute = self.substitute[0]
        self.indexes = [
            str(index) for index in range(1, len(self.view.menu_choices) + 1)
        ]
        self.possible_commands = ["delete-", s.BACK_TO_MENU, s.QUIT_APP]

    def display(self):
        """Display the menu."""
        return self.view.display_delete_substitutes(
            substituted_name=self.substituted.name,
            substitute_name=self.substitute.name,
        )

    def get_input(self):
        """Get the input."""
        self.view.input_delete_substitutes()
        choice = input(self.view.msg_choice)
        if choice == "m":
            return s.BACK_TO_MENU
        if choice == "q":
            return s.QUIT_APP
        if choice == "1":
            return "delete-"
        return choice

    def update(self, command: str) -> str:
        """Update the controller."""
        if command in self.indexes:
            return f"select-menu-{command}"

        if command in self.possible_commands:
            if command == "delete-":
                self.product.delete_substitutes(self.substitutes_id)
                return "delete"
            if command == s.QUIT_APP:
                self.walk = False
            if command == s.BACK_TO_MENU:
                return s.BACK_TO_MENU
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command