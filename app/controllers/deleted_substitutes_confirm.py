#!/usr/bin/env python
"""DeletedSubstitutesConfirm module."""
from app import settings as s
from app.views.view_deleted_substitutes_confirm import ViewDeletedSubstitutesConfirm
from app.models.product import Product


class DeletedSubstitutesConfirm:
    """Deleted substitutes confirm class."""

    def __init__(self):
        """Init."""
        self.view: ViewDeletedSubstitutesConfirm = ViewDeletedSubstitutesConfirm()
        self.product: Product = Product()

        self.indexes = [
            str(index) for index in range(1, len(self.view.menu_choices) + 1)
        ]
        self.possible_commands = ["back-to-menu", s.QUIT_APP]

    def display(self):
        """Display the menu."""
        return self.view.display_deleted_substitutes_confirm()

    def get_input(self):
        """Get the input."""
        self.view.input_deleted_substitutes_confirm()
        choice = input(self.view.msg_choice)
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str) -> str:
        """Update the controller."""
        if command in self.indexes:
            return f"select-menu-{command}"

        if command in self.possible_commands:
            if command == s.QUIT_APP:
                self.walk = False
            if command == "back-to-menu":
                return "back-to-menu"
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command