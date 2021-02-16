#!/usr/bin/env python
"""Select menu module."""
from app.settings import MENU_CHOICES, QUIT_APP, MSG_ERROR
from app.views.view_menu import ViewMenu


class SelectMenu:
    """Select menu class."""

    def __init__(self):
        """Init."""
        self.view: ViewMenu = ViewMenu()
        self.indexes = [str(index) for index in range(1, len(MENU_CHOICES) + 1)]
        self.possible_commands = [QUIT_APP]  # settings

    def get_input(self):
        """Get the input."""
        choice = input(self.view.get_input_message())
        if choice == "q":
            return QUIT_APP
        return choice

    def update(self, command: str):
        """Select menu."""
        if command in self.indexes:
            return f"select-menu-{command}"

        elif command in self.possible_commands:
            if command == QUIT_APP:
                self.walk = False
        else:
            return MSG_ERROR
        return command

    def display(self):
        """Display the menu."""
        return self.view.display_menu_principal()
