#!/usr/bin/env python
"""App file with Application class."""
from typing import Dict

from app import settings as s

from app.controllers.select_menu import SelectMenu
from app.controllers.select_category import SelectCategory
from app.controllers.select_product import SelectProduct
from app.controllers.select_substitute import SelectSubstitute
from app.controllers.select_saved_products import SelectSavedProducts
from app.controllers.save_substitute import SaveSubstitute
from app.controllers.select_favorites import SelectFavorites


class Application:
    """Pur Beurre app class."""

    Controllers: Dict[int, object] = {1: SelectCategory, 2: SelectSavedProducts}

    def __init__(self):
        """Init."""
        self.controller = SelectMenu()
        self.walk = True

    def run(self):
        """Run main method."""
        while self.walk:
            self.controller.display()
            command = self.controller.get_input()
            command = self.controller.update(command)
            self.update(command)

    def update(self, command: str):
        """Update."""
        if command.startswith("select-menu-"):
            command = command[-1]
            controller = [
                instance
                for index, instance in self.Controllers.items()
                if index == int(command)
            ][0]
            self.controller = controller()

        if command.startswith("back-to-menu"):
            self.controller = SelectMenu()

        if command.startswith("select-category-"):
            category_id = int(command.replace("select-category-", ""))
            self.controller = SelectProduct(category_id=category_id)

        if command == "save":
            self.controller = SaveSubstitute()

        if command.startswith("selected-product-"):
            product_id = int(command.replace("selected-product-", ""))
            self.controller = SelectSubstitute(product_id=product_id)

        if command.startswith("substitute-substituted-"):
            command = command.replace("substitute-substituted-", "")
            index = command.index("&")
            substitute_id = int(command[:index])
            substituted_id = int(command[index + 1 :])
            self.controller = SelectFavorites(
                substitute_id=substitute_id, substituted_id=substituted_id
            )

        if command == s.MSG_ERROR:
            s.ERROR = True
        else:
            s.ERROR = False

        if command == s.QUIT_APP:
            self.walk = False
