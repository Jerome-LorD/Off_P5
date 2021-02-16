#!/usr/bin/env python
"""Select detail product module."""
from app.settings import QUIT_APP, MSG_SAVE, MSG_ERROR

from app.models.product import Product
from app.views.main_page import View


class SelectSubstitute:
    """Select substitute."""

    def __init__(self, instance):
        """Init."""
        self.product: Product = Product()
        self.view: View = View()
        self.instance = instance[0]
        self.substitute = self.product.find_substitute(
            selected_product=self.instance.pk
        )
        self.indexes = [str(index) for index in range(1, len(MSG_SAVE) + 1)]
        self.possible_commands = ["back-to-menu", QUIT_APP]  # settings

    def display(self):
        """Display the substitute."""
        if self.instance.nutriscore == "a":
            self.view.display_no_better_nutriscore()
        elif (
            self.instance.nutriscore != "a"
            and self.substitute.nutriscore == self.instance.nutriscore
        ):
            self.view.display_no_subsitute()
        else:
            self.view.display_subsitute(details=self.substitute)

    def get_input(self):
        """Get input."""
        choice = input(self.view.input_save())
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return QUIT_APP
        return choice

    def update(self, command: str):
        """Update the controller."""
        if command in self.indexes:
            # command = self.categories[int(command) - 1]
            # if command == "save":
            if self.substitute:
                self.product.save_substitute(self.instance.pk, self.substitute.pk)
                return "save"
            else:
                self.product.save_substitute(self.instance.pk, self.instance.pk)
                return "save"
            # if command == "menu":
            #     return "menu"

        elif command in self.possible_commands:
            if command == QUIT_APP:
                self.walk = False
            if command == "back-to-menu":
                return "back-to-menu"
        else:
            return MSG_ERROR
        return command
