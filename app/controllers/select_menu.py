#!/usr/bin/env python
"""Select menu module."""
from app import settings as s
from app.views.view import View
from app.views.view_menu import ViewMenu


class SelectMenu:
    """Select menu class."""

    def __init__(self):
        """Init."""
        self.view: View = View()
        self.view_menu: ViewMenu = ViewMenu()
        self.indexes = [
            str(index) for index in range(1, len(self.view.menu_choices) + 1)
        ]
        self.possible_commands = [s.QUIT_APP]

    def display(self):
        """Display the menu."""
        return self.view_menu.display_main_menu()

    def get_input(self):
        """Get the input."""
        self.view_menu.input_message_menu()
        choice = input(self.view.msg_choice)
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str) -> str:
        """Update the controller."""
        if command in self.indexes:
            return f"select-menu-{command}"

        elif command in self.possible_commands:
            if command == s.QUIT_APP:
                self.walk = False
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command
