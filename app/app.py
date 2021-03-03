#!/usr/bin/env python
"""App file with Application class."""
from typing import List, Any

from app import settings as s

from app.controllers.select_menu import SelectMenu
from app.controllers.select_category import SelectCategory
from app.controllers.select_product import SelectProduct
from app.controllers.select_substitute import SelectSubstitute
from app.controllers.select_saved_products import SelectSavedProducts
from app.controllers.save_substitute import SaveSubstitute
from app.controllers.select_favorites import SelectFavorites
from app.controllers.delete_substitutes import DeleteSubstitutes
from app.controllers.deleted_substitutes_confirm import DeletedSubstitutesConfirm


class Application:
    """Pur Beurre app class.

    The Application class is the context,
    a controller is a strategy.
    """

    MenuConttrollers: List[Any] = [SelectCategory, SelectSavedProducts]

    def __init__(self):
        """Init."""
        self.controller = SelectMenu()
        self.walk = True

    def run(self):
        """Run main method."""
        while self.walk:
            self.controller.display()
            command = self.controller.get_input()
            self.update(command)

    def update(self, command: str):
        """Update."""
        command = self.controller.update(command)

        if command.startswith("select-menu-"):
            menu_index = int(command.replace("select-menu-", ""))
            controller = self.MenuConttrollers[menu_index - 1]
            self.controller = controller()

        if command.startswith("back-to-menu"):
            self.controller = SelectMenu()

        if command.startswith("select-category-"):
            category_id = int(command.replace("select-category-", ""))
            self.controller = SelectProduct(category_id=category_id)

        if command.startswith("delete-substituted_id-substitute_id-"):
            command = command.replace("delete-substituted_id-substitute_id-", "")
            comm = command.split("&")
            substitutes_id, substituted_id, substitute_id = [int(pk) for pk in comm]
            self.controller = DeleteSubstitutes(
                substitutes_id=substitutes_id,
                substituted_id=substituted_id,
                substitute_id=substitute_id,
            )

        if command == "delete":
            self.controller = DeletedSubstitutesConfirm()

        if command == "save":
            self.controller = SaveSubstitute()

        if command.startswith("selected-product-"):
            product_id = int(command.replace("selected-product-", ""))
            self.controller = SelectSubstitute(product_id=product_id)

        if command.startswith("substitute-substituted-"):
            command = command.replace("substitute-substituted-", "")
            comm = command.split("&")
            substitute_id, substituted_id = [int(pk) for pk in comm]
            self.controller = SelectFavorites(
                substitute_id=substitute_id, substituted_id=substituted_id
            )

        if command == s.MSG_ERROR:
            s.ERROR = True
        else:
            s.ERROR = False

        if command == s.QUIT_APP:
            self.walk = False
