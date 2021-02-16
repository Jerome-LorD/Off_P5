#!/usr/bin/env python
"""Select detail product module."""
# from app.settings import QUIT_APP
from app.models.product import Product, ProductInstance

from app.views.main_page import View


class SelectDetail:
    """Select detail."""

    def __init__(self, product_id, category_id):
        """Init."""
        self.product: Product = Product()
        self.product_instance: ProductInstance = ProductInstance
        self.view: View = View()
        self.product_id = product_id
        self.category_id = category_id
        self.products = self.product.list(
            self.category_id, self.product.limit, self.product.offset
        )

    def select_detail(self):
        """Select products detail."""
        print("Dans select_detail", self.product.product_instance_lst)
        for instance in self.product.product_instance_lst:
            print(instance.name)

    def display(self):
        """Display."""
        details = self.products[self.product_id - 1]
        breakpoint()
        self.view.display_detail(details=details)


if __name__ == "__main__":
    s = SelectDetail(20, 30)
    s.select_detail()
