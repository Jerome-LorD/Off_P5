#!/usr/bin/env python
"""View menu module."""
from app.settings import HEADER, DASHES


class ViewMenu:
    """Class ViewMenu."""

    def __init__(self):
        """Init."""
        self.choices = {
            "1": "Quel aliment souhaitez-vous remplacer ?",
            "2": "Retrouver mes aliments substitués.",
        }

    def header(self):
        """Display the header."""
        return f"\n{DASHES}\n{HEADER}\n{DASHES}"

    def display_menu_principal(self):
        """Get the menu principal."""
        print(self.header())
        print("\nMenu principal\n")

    def get_input_message(self):
        """Get the input message."""
        return "\n".join([f"{k}: {v} " for k, v in self.choices.items()])
