#!/usr/bin/env python
"""Main page controller."""
from app.settings import QUIT_APP
from app.views.main_page import View
from app.models.product import Product
from app.models.category import Category


class Controller:
    """Main page."""

    def __init__(self):  # , choice: str):
        """Init."""
        # self.choice = choice
        self.view = View()
        self.product: Product = Product()
        self.category: Category = Category()

        # self.products = self.product.list(4, self.product.page_index, 50)

    def display(self, choice):
        """Do something."""
        self.view.display(choice)

    def get_input_category(self):
        """Get input.

        Dans une class SelectCategory -> init(self, category: Category)
        """
        categories = self.category.retrieve()
        command = None
        command = input(
            "\n".join([f"{nb}. {item} " for nb, item in enumerate(categories, 1)])
        )
        if command == QUIT_APP:
            print("Msg d'au revoir.")
            self.category.walk = False
        else:
            command = categories[int(command) - 1]

        return command
        # item_choice = None

        # while not item_choice:
        #     products = self.model.list(4, self.model.page_index, 50)

        #     # print(f"Page {self.page_index} - Affichage des résultats\n")
        #     item_choice = input(
        #         "\n".join([f"{nb}. {item} " for nb, item in enumerate(products, 1)])
        #     )

        #     return item_choice

    # le plus simple serait de proposer "next" et "previous"
    # pour un menu qui ne bouge pas, on peut imaginer une même vue mais qui ne fait
    # qu'avoir une liste de produit différente entre chaque page
    # que le controller lui passerait en fonction de la navigation de l'utilisateur


#     def get_input_product(self):
#         """Get input.

#         Dans une class SelectProduct -> init(self, product: Product)
#         """
#         cat_id = self.get_input_category()
#         product, item_choice = Product().navig(cat_id, 30)
#         # command = None
#         try:
#             command = int(
#                 input(
#                     "\n".join([f"{nb}. {item} " for nb, item in enumerate(product, 1)])
#                 )
#             )
#         except ValueError:
#             print("Error msg")
#         else:
#             if command == QUIT_APP:
#                 print("Msg d'au revoir.")
#         return command

#     def get_pages(self, item_choice):
#         """Get pages."""
#         total_lines = self.model.list(4, self.model.page_index, 50)
#         nb_pages = len(self.model.paging(total_lines))  # , limit))
#         pages_possibles = [page_number + 1 for page_number in range(nb_pages)]
#         max_nb_page = max(pages_possibles)
#         min_nb_page = min(pages_possibles)
#         if not item_choice:
#             index = None
#             try:
#                 index = int(
#                     input(
#                         f"[PAGE {self.page_index}] changer de page\
#  [{min_nb_page} à {max_nb_page}] "
#                     )
#                 )
#             except Exception:
#                 print("Saisissez le numéro de la page que vous voulez consulter.")

#             if index in pages_possibles:
#                 self.page_index = index
#             else:
#                 self.page_index = min_nb_page
#         else:
#             return products, item_choice


# if __name__ == "__main__":
# page = MainPageController()
#     page.display()
# page.get_input_category()
# page.get_input_product()
