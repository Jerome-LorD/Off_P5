#!/usr/bin/env python
"""Select category module."""
from app import settings as s

from app.models.category import Category
from app.views.main_page import View


class SelectCategory:
    """Select category."""

    def __init__(self):
        """Init."""
        self.view = View()
        self.categories = Category.retrieve()
        self.indexes = [str(index) for index in range(1, len(self.categories) + 1)]
        self.possible_commands = [s.QUIT_APP]

    def display(self):
        """Display."""
        self.view.display_categories(categories=self.categories)

    def get_input(self):
        """Get input."""
        choice = self.view.input_message(self.categories)
        choice = input(s.MSG_CHOICE)
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str):
        """Update the controller."""
        if command in self.indexes:
            command = self.categories[int(command) - 1]
            return f"select-category-{command.product_id}"

        elif command in self.possible_commands:
            if command == s.QUIT_APP:
                self.walk = False
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command
