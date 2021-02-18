#!/usr/bin/env python
"""View menu module."""
from app import settings as s
from colorama import init
from termcolor import colored


init()


class ViewMenu:
    """Class ViewMenu."""

    def __init__(self):
        """Init."""

    def header(self):
        """Display the header."""
        return f"\n{s.DASHES}\n{s.HEADER}\n{s.DASHES}"

    def display_main_menu(self):
        """Display the main menu."""
        print(self.header())
        print("\nMenu principal\n")
        if s.ERROR:
            print(s.MSG_ERROR)

    def input_message_menu(self):
        """Input message menu."""
        choice = "\n".join(
            [
                colored(f"{index}", "yellow") + f". {item} "
                for index, item in s.MENU_CHOICES.items()
            ]
        )
        print(choice)
