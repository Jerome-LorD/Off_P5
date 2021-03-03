#!/usr/bin/env python
"""ViewDeletedSubstitutesConfirm module."""
from colorama import init  # type: ignore
from termcolor import colored

from app.views.view import View
from app import settings as s

init(autoreset=True)


class ViewDeletedSubstitutesConfirm(View):
    """View deleted substitutes confirm class."""

    def __init__(self):
        """Init."""
        super().__init__()

    def display_deleted_substitutes_confirm(self):
        """Display confirmation of the removal of favorites from the database."""
        print(self.header())
        print(f'\n{colored(self.justify(s.DEL_CONFIRM, 3), "green")}\n')

    def input_deleted_substitutes_confirm(self):
        """Input the choices menu."""
        choice = "\n".join(
            [
                f"{colored(self.justify(str(index), 1), 'yellow')}. {item}"
                for index, item in enumerate(self.menu_choices, 1)
            ]
        )
        print(choice)
        print(f"{s.CR}{self.footer}")
        if s.ERROR:
            print(self.msg_error)
        print(self.back, self.quit)