#!/usr/bin/env python
"""ViewMenu module."""
from colorama import init  # type: ignore
from termcolor import colored

from app.views.view import View
from app import settings as s

init(autoreset=True)


class ViewMenu(View):
    """View Menu class."""

    def __init__(self):
        """Init."""
        super().__init__()

    def display_main_menu(self):
        """Display the main menu."""
        print(self.header())

    def input_message_menu(self):
        """Input the menu message."""
        print()
        choice = "\n".join(
            [
                f"{colored(index, 'yellow')}. {item}"
                for index, item in enumerate(self.menu_choices, 1)
            ]
        )
        print(choice)
        print(f"{s.CR}{self.footer}")
        if s.ERROR:
            print(self.msg_error)
        print(self.quit)
