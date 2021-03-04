#!/usr/bin/env python
"""ViewSaveSubstitute module."""
from colorama import init  # type: ignore
from termcolor import colored

from app.views.view import View
from app import settings as s

init(autoreset=True)


class ViewSaveSubstitute(View):
    """View save substitute class."""

    def __init__(self):
        super().__init__()

    def display_save_substitute(self):
        """Display confirmation of saving substitute."""
        print(self.header())
        print(f"\n{self.confirm_title}\n")
        print(f"\n{self.save_confirm}\n")
        print(f"{s.CR}{self.footer}")
        print(self.back, self.quit)
        if s.ERROR:
            print(self.msg_error)

    def input_saved(self):
        """Input the saved message."""
        self.menu_choices[0] = s.OTHER_ITEM
        choice = "\n".join(
            [
                colored(str(index), "yellow") + ". " + item
                for index, item in enumerate(self.menu_choices, 1)
            ]
        )
        print(choice)
