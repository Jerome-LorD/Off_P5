#!/usr/bin/env python
"""SubstituteAlreadyInDb module."""
from app.settings import MSG_SAVE
from app.views.main_page import View
from app.models.product import Product

class SubstituteAlreadyInDb:
    """SubstituteAlreadyInDb class."""

    def __init__(self):
        """Init."""
        self.view: View = View()
        self.product: Product = Product()

    def display(self):
        """Display."""
        return self.view.display_substitute_already_in_db()

    def get_input(self):
        """Get the input."""
        return input(self.view.input_already_in_db())

    def update(self):
        """Update."""
        pass
