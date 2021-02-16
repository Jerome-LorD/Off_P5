#!/usr/bin/env python
"""Category file."""
import os

from dotenv import load_dotenv, find_dotenv

from app.models.database import Database


load_dotenv(find_dotenv())


off_user = os.getenv("OFF_USER")
off_password = os.getenv("OFF_PASSWD")
off_database = os.getenv("OFF_DB")


class Category:
    """Category class."""

    def __init__(
        self,
        name: str = "",
        nutriscore: str = "",
        brand: str = "",
        stores: str = "",
        url: str = "",
        id: int = None,
        category_id: int = None,
        bonus2: int = None,
    ):
        """Init."""
        self.name = name
        self.nutriscore = nutriscore
        self.brand = brand
        self.stores = stores
        self.url = url
        self.product_id = id
        self.category_id = category_id
        self.bonus2 = bonus2

        # self.command = SelectCategory().get_input()

        self.walk: bool = True

    def __str__(self):
        """Return name as default value."""
        return f"{self.name}"

    def __repr__(self):
        """Return Format str."""
        # return self.__str__()
        return f"{self.name} - {self.nutriscore} - {self.brand} - {self.stores}\
 - {self.url} - {self.product_id} - {self.category_id}"

    @classmethod
    def retrieve(cls):
        """Select the 30  categories."""
        cls.db = Database(off_user, off_password, off_database)
        cls.db.cursor.execute(
            "SELECT categories.name, categories.id, COUNT(products.id) as total_products\
                        FROM categories_products\
                        INNER JOIN products\
                        ON categories_products.products_id = products.id\
                        JOIN categories\
                        ON categories.id = categories_products.categories_id\
                        GROUP BY categories.name\
                        ORDER BY total_products  DESC LIMIT 30"
        )

        return [Category(name=line[0], id=line[1]) for line in cls.db.cursor.fetchall()]

    @classmethod
    def find_best_category(cls, pk, offset):
        """Find the best category."""
        cls.db = Database(off_user, off_password, off_database)
        cls.db.cursor.execute(
            "SELECT p.name, ns.type, p.brand, p.stores, p.url, p.id,\
                             c.id as category_with_the_fewest_products, (\
                        SELECT COUNT(p_in.id) tot_in\
                        FROM products p_in\
                        JOIN categories_products cp_in\
                        ON p_in.id = cp_in.products_id\
                        JOIN categories c_in\
                        ON c_in.id = cp_in.categories_id\
                        where c_in.id in (category_with_the_fewest_products) \
                        GROUP BY c_in.name\
                    ) as tot_produtcs_in_fewest_category\
            FROM products p\
            JOIN categories_products cp\
            ON cp.products_id = p.id\
            JOIN categories c\
            ON cp.categories_id = c.id\
            JOIN nutriscore ns\
            ON p.nutriscore_id = ns.id\
            WHERE p.id = %s\
            GROUP BY tot_produtcs_in_fewest_category ASC LIMIT 1 OFFSET %s",
            (
                pk,
                offset,
            ),
        )
        return [Category(*line) for line in cls.db.cursor.fetchall()]

    # l'input sert à modifier les controllers ou quitter l'application dans les
    # grandes lignes. modifier un controller = changer de page = changer de vue

    # - dans le controller de selection des catégories, tu:
    # -- affiche les catégories
    # -- affiches les commandes
    # -- récupère l'input utilisateur
    # -- et retourne une commande associée
    # -- l'application récupère la commande et  dans sa méthode update, peut la décrire
    #  et mettre à jour le controller pour aller à la page de catégorie associée

    def get_command(self, command):
        """Récupère la commande de l'input de SelectCategory."""
        categories = Category.retrieve()
        reponse = categories[int(command) - 1]
        return reponse.product_id

    # def update(self):
    #     """Update."""
    #     if QUIT_APP == "q":
    #         self.walk = False


# if __name__ == "__main__":
#     categories = Category().retrieve()

#     choice_category = input(
#         "\n".join([f"{nb}. {item} " for nb, item in enumerate(categories, 1)])
#     )
#     choix = categories[int(choice_category) - 1]

#     print(choix.id)
# print(category.retrieve())

# breakpoint()
# for nb, item in enumerate(category.retrieve(), 1):
#     print(f"{nb} - {item}")

# for i, j in enumerate(category.retrieve(), 1):
#     print(i, j)

# for i in range(len(category)):
#     print(category[i])
