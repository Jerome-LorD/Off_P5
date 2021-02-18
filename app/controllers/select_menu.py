#!/usr/bin/env python
"""Select menu module."""
from app import settings as s
from app.views.view_menu import ViewMenu


class SelectMenu:
    """Select menu class."""

    def __init__(self):
        """Init."""
        self.view: ViewMenu = ViewMenu()
        self.indexes = [str(index) for index in range(1, len(s.MENU_CHOICES) + 1)]
        self.possible_commands = [s.QUIT_APP]

    def get_input(self):
        """Get the input."""
        choice = self.view.input_message_menu()
        choice = input(s.MSG_CHOICE)
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str):
        """Select menu."""
        if command in self.indexes:
            return f"select-menu-{command}"

        elif command in self.possible_commands:
            if command == s.QUIT_APP:
                self.walk = False
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command

    def display(self):
        """Display the menu."""
        return self.view.display_main_menu()
