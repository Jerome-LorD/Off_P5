#!/usr/bin/env python
"""ViewDeleteSubstitutes module."""
from colorama import init  # type: ignore
from termcolor import colored

from app.views.view import View
from app import settings as s

init(autoreset=True)


class ViewDeleteSubstitutes(View):
    """View delete substitute class."""

    def __init__(self):
        super().__init__()

    def display_delete_substitutes(self, substituted_name, substitute_name):
        """Display an alert message to confirm the deletion."""
        print(self.header())
        print(
            f'\n{self.justify("Souhaitez-vous vraiment supprimer", 3)}\
 {colored(substituted_name, "cyan")}\n{self.justify("et", 3)}\
 {colored(substitute_name, "cyan")} de vos favoris ?\n\n{self.del_alert}\n'
        )

    def input_delete_substitutes(self):
        """Input the choices."""
        self.menu_choices[0] = s.DELETE_ITEM
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
        print(self.back, self.quit)
