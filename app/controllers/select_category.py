#!/usr/bin/env python
"""Select category module."""
from app.settings import QUIT_APP, MSG_ERROR

from app.models.category import Category
from app.views.main_page import View


class SelectCategory:
    """Select category."""

    def __init__(self):
        """Init."""
        self.view = View()
        self.categories = Category.retrieve()
        self.indexes = [str(index) for index in range(1, len(self.categories) + 1)]
        self.possible_commands = [QUIT_APP]

    def get_input(self):
        """Get input."""
        choice = input(self.view.input_message(self.categories))
        if choice == "q":
            return QUIT_APP
        return choice

    def update(self, command: str):
        """Update the controller."""
        if command in self.indexes:
            command = self.categories[int(command) - 1]
            return f"select-category-{command.product_id}"

        elif command in self.possible_commands:
            if command == QUIT_APP:
                self.walk = False
        else:
            return MSG_ERROR
        return command

    def display(self):
        """Display."""
        self.view.display_categories(categories=self.categories)
