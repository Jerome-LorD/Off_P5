#!/usr/bin/env python
"""App file with Application class."""

from typing import Dict

from app import settings as s

from app.controllers.select_menu import SelectMenu
from app.controllers.select_category import SelectCategory
from app.controllers.select_product import SelectProduct
from app.controllers.select_detail_tst import SelectDetailTst
from app.controllers.select_substitute import SelectSubstitute
from app.controllers.select_saved_products import SelectSavedProducts
from app.controllers.save_substitute import SaveSubstitute
from app.controllers.select_best_product import SelectBestProduct

from app.models.product import Product
from app.views.main_page import View


class Application:
    """Pur Beurre app class."""

    Controllers: Dict[int, object] = {1: SelectCategory, 2: SelectSavedProducts}

    def __init__(self):
        """Init."""
        self.controller = SelectMenu()
        self.view = View()
        self.product: Product = Product()
        self.walk = True

        self.category_id: int = None
        self.product_id: int = None

    def run(self):
        """Run main method."""
        while self.walk:
            self.controller.display()
            command = self.controller.get_input()
            command = self.controller.update(command)
            self.update(command)

    def update(self, command: str):
        """Update."""
        if isinstance(command, str) and command.startswith("select-menu-"):
            command = command[-1]
            controller = [
                instance
                for index, instance in self.Controllers.items()
                if index == int(command)
            ][0]
            self.controller = controller()

        if str(command).startswith("back-to-menu"):
            self.controller = SelectMenu()

        if str(command).startswith("select-category-"):
            self.category_id = int(command.replace("select-category-", ""))
            self.controller = SelectProduct(category_id=self.category_id)

        if command == "save":
            self.controller = SaveSubstitute()

        if isinstance(command, tuple):
            if command[1] == "best-product":
                self.controller = SelectBestProduct(instance=command)
            if command[1] == "product":
                self.controller = SelectDetailTst(instance=command)
            if command[1] == "substitute":
                self.controller = SelectSubstitute(instance=command)

        if command == s.MSG_ERROR:
            s.ERROR = True
        else:
            s.ERROR = False

        if command == s.QUIT_APP:
            self.walk = False
