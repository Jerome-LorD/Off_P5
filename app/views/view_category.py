#!/usr/bin/env python
"""ViewCategory module."""
from colorama import init  # type: ignore
from termcolor import colored

from app.views.view import View
from app import settings as s

init(autoreset=True)


class ViewCategory(View):
    """View Menu class."""

    def __init__(self):
        super().__init__()

    def display_categories(self):
        """Display the categories."""
        print(self.header())
        print(f"\n{self.select_category}\n")

    def input_categories(self, categories):
        """Input the categories."""
        choice = "\n".join(
            [
                colored(self.justify(str(index), 1), "yellow") + ". " + item.name
                for index, item in enumerate(categories, 1)
            ]
        )
        print(choice)
        print(f"{s.CR}{self.footer}")
        if s.ERROR:
            print(self.msg_error)
        print(self.back, self.quit)
