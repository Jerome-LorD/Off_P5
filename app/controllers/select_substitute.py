#!/usr/bin/env python
"""Select detail product module."""
from app import settings as s
from app.models.product import Product
from app.views.view import View


class SelectSubstitute:
    """Select substitute.

    qui va devenir SelectDetails

    Get the product instance and then, whith the product id, the substitute instance
    is found.
    """

    def __init__(self, product_id):
        """Init."""
        self.product: Product = Product()
        self.view: View = View()
        self.product_id = product_id
        self.substitute = self.product.find_substitute(selected_product=self.product_id)
        self.substituted = self.product.retrieve(self.product_id)
        self.substituted = self.substituted[0]
        self.indexes = [str(index) for index in range(1, len(s.MSG_SAVE) + 1)]
        self.possible_commands = [
            "save",
            "select-menu-2",
            s.BACK_TO_MENU,
            s.QUIT_APP,
        ]

    def display(self):
        """Display the substitute."""
        if self.substituted.nutriscore == "a":
            self.view.display_no_better_nutriscore(product=self.substituted)
        elif (
            self.substituted.nutriscore != "a"
            and self.substitute.nutriscore == self.substituted.nutriscore
        ):
            self.view.display_no_subsitute(product=self.substituted)
        else:
            self.view.display_details(
                substituted=self.substituted,
                substitute=self.substitute,
            )

    def get_input(self):
        """Get input.

        Ask for save or find the saved substitutes.
        """
        if self.substituted.nutriscore == "a" or (
            self.substituted.nutriscore != "a"
            and self.substitute.nutriscore == self.substituted.nutriscore
        ):
            choice = self.view.input_saved()
            choice = input(s.MSG_CHOICE)
            if choice == "m":
                return s.BACK_TO_MENU
            if choice == "q":
                return s.QUIT_APP
        else:
            choice = self.view.input_save()
            choice = input(s.MSG_CHOICE)
            if choice == "m":
                return s.BACK_TO_MENU
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

        Save the product in db if requested.
        """
        if command in self.indexes:
            if command == "1":
                return f"select-menu-{command}"
            if command == "2":
                return f"select-menu-{command}"

        if command in self.possible_commands:
            if command == "save":
                if self.substitute:
                    if not self.product.is_substitute_in_db(self.substitute.pk):
                        if self.substitute.nutriscore < self.substituted.nutriscore:
                            self.product.save_substitute(
                                self.substituted.pk, self.substitute.pk
                            )
                        return "save"

            if command == s.QUIT_APP:
                self.walk = False
            if command == s.BACK_TO_MENU:
                return s.BACK_TO_MENU
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command
