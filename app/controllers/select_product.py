#!/usr/bin/env python
"""Select product module."""
from app.settings import NEXT_PAGE, PREVIOUS_PAGE, QUIT_APP, MSG_ERROR
from app.models.product import Product

from app.views.main_page import View


class SelectProduct:
    """Select product."""

    def __init__(self, category_id):
        """Init."""
        self.view = View()
        self.product = Product()
        self.category_id = int(category_id)
        self.product.get_total_lines(self.category_id)

        self.products = Product.list(
            self.category_id, self.product.limit, self.product.offset
        )

        self.indexes = [str(index) for index in range(1, len(self.products) + 1)]
        self.possible_commands = ["next-page", "previous-page", QUIT_APP]  # settings

    def get_input(self):
        """Get input."""
        choice = input(self.view.input_message(self.products))
        if choice == "n":
            return NEXT_PAGE
        if choice == "p":
            return PREVIOUS_PAGE
        if choice == "q":
            return QUIT_APP
        return choice

    def update(self, command: str):
        """Update the commands."""
        if command in self.indexes:
            instance = self.products[int(command) - 1]
            return instance, "product"

        elif command in self.possible_commands:
            if command == QUIT_APP:
                self.walk = False

            if command == NEXT_PAGE and self.product.has_next_page:
                self.product.page_index += 1

            if command == PREVIOUS_PAGE and self.product.has_previous_page:
                self.product.page_index -= 1

        else:
            return MSG_ERROR
        return command

    def display(self):
        """Display."""
        self.products = self.product.list(
            self.category_id, self.product.limit, self.product.offset
        )

        self.view.display_products(
            products=self.products,
            max_pages=self.product.max_pages,
            page=self.product.page_index,
        )


# s = SelectProduct(20)
# print(s.get_input())


# perso je mettrais une valeur par défaut à limit de la méthode list
# def list(cls, category_id, offset, limit=None):
#   if not limit:
#     limit = cls.limit
# limit pourrait être un attribut de classe du coup

# if command == "next-page" and self.product.has_next_page:  # normalement get-input
# retourne une commande lisible !
# product has_next quoi ? il faut que la méthode ou la propriété se suffise en soi
# self.products = self.product.list(self.category_id, next_page=True)
# pas besoin de plus ici ! la classe product se charge de mettre à jour l'indexe
# et l'offset tout seul comme un grand

# en gros, beaucoup de code géré en dehors de la méthode list qui aurait tout
# intérêt à être géré dans la méthode list :slight_smile:
# ou tu pourrais créer une méthode change_page pour différer de la méthode list
