#!/usr/bin/env python
"""Select detail product module."""
from app import settings as s
from app.models.product import Product
from app.views.main_page import View


class SelectSubstitute:
    """Select substitute.

    Get the product instance and then, whith the product id, the substitute instance
    is found.
    """

    def __init__(self, instance):
        """Init."""
        self.product: Product = Product()
        self.view: View = View()
        self.prdt_instance = instance[0]
        self.substitute = self.product.find_substitute(
            selected_product=self.prdt_instance.pk
        )
        self.indexes = [str(index) for index in range(1, len(s.MSG_SAVE) + 1)]
        self.possible_commands = ["save", "select-menu-2", "back-to-menu", s.QUIT_APP]

    def display(self):
        """Display the substitute."""
        if self.prdt_instance.nutriscore == "a":
            self.view.display_no_better_nutriscore()
        elif (
            self.prdt_instance.nutriscore != "a"
            and self.substitute.nutriscore == self.prdt_instance.nutriscore
        ):
            self.view.display_no_subsitute()
        else:
            self.view.display_subsitute(details=self.substitute)

    def get_input(self):
        """Get input.

        ask for save or find the saved substitutes.
        """
        choice = self.view.input_save()
        choice = input(s.MSG_CHOICE)
        if choice == "m":
            return "back-to-menu"
        if choice == "q":
            return s.QUIT_APP
        if choice in self.indexes:
            if choice == "1":
                return "save"
            if choice == "2":
                return "select-menu-2"
        return choice

    def update(self, command: str):
        """Update the controller.

        Prompt and save the product in db if requested.
        """
        if command in self.possible_commands:
            if command == "select-menu-2":
                return command

            if command == "save":
                if self.substitute:
                    if self.substitute.nutriscore < self.prdt_instance.nutriscore:
                        self.product.save_substitute(
                            self.prdt_instance.pk, self.substitute.pk
                        )
                        return "save"
                    else:
                        self.product.save_substitute(
                            self.prdt_instance.pk, self.prdt_instance.pk
                        )
                        return "save"
            if command == s.QUIT_APP:
                self.walk = False
            if command == "back-to-menu":
                return "back-to-menu"
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command
