#!/usr/bin/env python
"""Select product module."""
from app import settings as s
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
        self.possible_commands = ["next-page", "previous-page", s.QUIT_APP]

    def get_input(self):
        """Get input."""
        choice = self.view.input_message(self.products)
        choice = input(s.MSG_CHOICE)
        if choice == "n":
            return s.NEXT_PAGE
        if choice == "p":
            return s.PREVIOUS_PAGE
        if choice == "q":
            return s.QUIT_APP
        return choice

    def update(self, command: str):
        """Update the commands."""
        if command in self.indexes:
            instance = self.products[int(command) - 1]
            return instance, "product"

        elif command in self.possible_commands:
            if command == s.QUIT_APP:
                self.walk = False

            if command == s.NEXT_PAGE and self.product.has_next_page:
                self.product.page_index += 1

            if command == s.PREVIOUS_PAGE and self.product.has_previous_page:
                self.product.page_index -= 1

        else:
            s.ERROR = True
            return s.MSG_ERROR
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
