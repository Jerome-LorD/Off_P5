#!/usr/bin/env python
"""Select detail product module."""
from app import settings as s
from app.models.product import Product
from app.views.view_substitute import ViewSubstitute


class SelectSubstitute:
    """Select substitute.

    Get the product instance and then, whith the product id, the substitute
    instance is found.
    """

    def __init__(self, product_id):
        """Init."""
        self.product: Product = Product()
        self.view: ViewSubstitute = ViewSubstitute()
        self.product_id = product_id
        self.substitute = self.product.find_substitute(selected_product=self.product_id)
        self.substituted = self.product.retrieve(self.product_id)
        self.substituted = self.substituted[0]
        self.is_there_a_couple = True
        if (
            self.substituted.nutriscore == "a"
            or self.substituted.nutriscore == self.substitute.nutriscore
        ):
            self.is_there_a_couple = False
        self.indexes = [
            str(index) for index in range(1, len(self.view.menu_choices) + 1)
        ]
        self.possible_commands = [
            "select-menu-",
            "save",
            s.BACK_TO_MENU,
            s.QUIT_APP,
        ]

    def display(self):
        """Display the substitute."""
        if self.is_there_a_couple:
            self.view.display_details(
                substituted=self.substituted,
                substitute=self.substitute,
            )
        else:
            self.view.display_no_subsitute(product=self.substituted)

    def get_input(self):
        """Get input.

        Ask for save the substitute or find the saved substitutes.
        """
        self.view.input_save(couple=self.is_there_a_couple)
        choice = input(self.view.msg_choice)
        if choice == "m":
            return s.BACK_TO_MENU
        if choice == "q":
            return s.QUIT_APP
        if choice in self.indexes:
            if self.is_there_a_couple:
                if choice == "1":
                    return "save"
                if choice == "2":
                    return f"select-menu-{choice}"
            else:
                return f"select-menu-{choice}"
        return choice

    def update(self, command: str) -> str:
        """Update the controller.

        Save the product in db if requested.
        """
        if command.startswith("select-menu-") or command in self.possible_commands:
            if command.startswith("select-menu-"):
                menu_index = command.replace("select-menu-", "")
                return f"select-menu-{menu_index}"

            if command == "save":
                if self.is_there_a_couple:
                    self.product.save_substitute(
                        self.substituted.pk, self.substitute.pk
                    )
                    return command
            if command == s.QUIT_APP:
                self.walk = False
            if command == s.BACK_TO_MENU:
                return s.BACK_TO_MENU
        else:
            s.ERROR = True
            return s.MSG_ERROR
        return command
