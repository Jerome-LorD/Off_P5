#!/usr/bin/env python
"""Select category module."""
from app import settings as s

from app.models.category import Category
from app.views.view_category import ViewCategory


class SelectCategory:
    """Select category."""

    def __init__(self):
        """Init."""
        self.view: ViewCategory = ViewCategory()
        self.categories = Category.retrieve()
        self.indexes = [str(index) for index in range(1, len(self.categories) + 1)]
        self.possible_commands = [s.BACK_TO_MENU, s.QUIT_APP]

    def display(self):
        """Display."""
        self.view.display_categories()

    def get_input(self):
        """Get input."""
        self.view.input_categories(categories=self.categories)
        choice = input(self.view.msg_choice)
        if choice == "m":
            return s.BACK_TO_MENU
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str) -> str:
        """Update the controller."""
        if command in self.indexes:
            category = self.categories[int(command) - 1]
            return f"select-category-{category.product_id}"

        elif command in self.possible_commands:
            if command == "back-to-menu":
                return s.BACK_TO_MENU
            if command == s.QUIT_APP:
                self.walk = False
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command
