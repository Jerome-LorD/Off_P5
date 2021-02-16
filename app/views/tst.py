# l = {"1": "controller_A-1", "2": "controller_B-2"}


# cmd = input("Lequel, 1 ou 2 ")
# for k, v in l.items():
#     if cmd == k:
#         print(v)
# import types


# class A:
#     def gag(self):
#         print("dans A")


# class B:
#     def gag(self):
#         print("dans B")


# class C:
#     def gag(self):
#         print("dans C")


# class Base:
#     cont = {1: A, 2: B, 3: C}

#     def get_input(self):
#         command = input("1. prop 1\n2. prop 2\n3. prop 3 ")
#         return f"prop-{command}"

#     def gag(self, command: str):
#         if command.startswith("prop-"):
#             command = command[-1]
#         return [
#             instance for item, instance in self.cont.items() if item == int(command)
#         ][0]


# b = Base()
# com = b.get_input()
# instance = [b.gag(com)()]
# print(type(instance))
# if str() in instance:
#     print("STR IN INSTANCE !")
# breakpoint()
# if not isinstance(instance, A):
#     instance.gag()
# else:
#     print("pas une instance.")

# met une valeur dans un tab si cette valeur n'est pas dedans
# Propose un input pour enregistrer
# MIEUX


class Db:
    def __init__(self):
        """Init.

        Si le pdt n'est pas en db, propose de l'insérer
        ["Sauvegarder le produit", "Revenir au menu principal"]

        Si le pdt est DEJA EN DB
        ["Consulter la liste des sauvegardes", "Revenir au menu principal"]

        Le truc est de replace() "Sauvegarder un produit"
        par "Consulter la liste des sauvegardes"

        menu = [
            item.replace("Sauvegarder le produit",
            "Consulter la liste des sauvegardes")
            ]
        Donc la condition est Si le produit est déja enregistré
        Et ce, qu'il soit en double sur la row ou unique sur une row (en substitut_id)
        """
        self.tab = ["abc"]
        # self.liste = ["choix 1", "choix 2", "choix 3", "choix 4"]
        self.liste = ["choix 1", "choix 2"]

        self.possible_commands = ["q"]
        self.run = True

    def display(self):

        self.menu = "\n".join([f"{k}. {v}" for k, v in enumerate(self.liste, 1)])
        # print(self.indexes)
        print(self.menu)

    def get_input(self):
        print(self.liste)
        self.indexes = [str(index) for index in range(1, len(self.liste) + 1)]
        self.choix = input("Choisissez l'index à enregistrer ")
        if self.choix in self.indexes:
            self.value = self.liste[int(self.choix) - 1]
            if self.value not in self.tab:
                print("La valeur est maintenant insérée en base de donnée.")
                if "choix 3" in self.liste:
                    self.liste = [
                        item.replace("choix 3", "choix 1") for item in self.liste
                    ]
            else:
                self.liste = [item.replace("choix 1", "choix 3") for item in self.liste]
            #     self.tab.append(self.value)
            #     self.liste.remove(self.value)
            #     print(f"la valeur {self.value} est maintenant dans la 'db'.")
            # elif self.value in self.tab:
            #     print("La valeur choisie est déjà en 'db'.")
            # elif len(self.tab) == len(self.liste):
            #     print("On a fait le tour !")
        elif self.choix in self.possible_commands:
            if self.choix == "q":
                self.run = False
        else:
            print("\nchoix impossible.\n")


db = Db()
db.run = True
while db.run:
    if len(db.tab) < 4:
        db.display()
        db.get_input()
        if len(db.tab) == 4:
            db.run = False

    print(f"\nLa db : {db.tab}")


class Menu:
    def __init__(self):
        self.histo = []
        self.cmd_possibles = ["choix 1", "choix 2", "choix 3", "choix 4"]
        self.menu = ["choix 1", "choix 2", "choix 3", "choix 4"]

    def display(self):
        print(self.menu)


# SELECT
#     linker.id,
#     substitute.name AS substitute_name,
#     substituted.name AS substituted_name
# FROM
#     substitute linker
#     INNER JOIN product substitute
#         ON linker.substitute_id = substitute.id
#     INNER JOIN product substituted
#         ON linker.substituted_id = substituted.id


# cursor.execute(f"SELECT id FROM nutriscore WHERE type = {product['nutriscore']}")
# nutriscore_id = cursor.fetchone[0]
# cursor.execute(f"INSERT INTO product (name, nutriscore_id, ...) VALUES ({name}, {nutriscore_id}, ...)")


# f"""INSERT INTO product(nutriscore_id, ...)
# VALUES (
#   (SELECT id
#    FROM nutriscore
#    WHERE type = {product['type']}
#   ),
#   ...,
# )
# """
# t = ["", "", "a"]

# offset = 0
# for i in t:

#     if i:
#         print(i, offset)
#         break
#     else:
#         offset += 1

#         print(offset)


# @property
# def max_pages(self):
#     pass

# self.page_index = 1


# @property
# def has_next(self):
#     if self.page_index < self.max_page:
#         return True
#     return False


# Using @property decorator
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature

#     @property
#     def temperature(self):
#         print("Getting value...")
#         return self._temperature

#     @temperature.setter
#     def temperature(self, value):
#         print("Setting value...")
#         if value < -273.15:
#             raise ValueError("Temperature below -273 is not possible")
#         self._temperature = value

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32


# # create an object
# human = Celsius(37)

# print(human.temperature)

# print(human.to_fahrenheit())

# coldest_thing = Celsius(-300)
