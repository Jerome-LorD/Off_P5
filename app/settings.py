#!/usr/bin/env python
"""Contains all p5 constants."""
from colorama import init
from termcolor import colored


init(autoreset=True)

DB_NAME = "offdb"

SQL_FILE = "offdb_p5.sql"

QUIT_APP = "quit-app"
NEXT_PAGE = "next-page"
PREVIOUS_PAGE = "previous-page"

MENU_CHOICES = {
    "1": "Faire une recherche d'aliment à remplacer",
    "2": "Chercher un substitut sauvegardé.",
}

HEADER = f'---{colored("        Pur Beurre App         ", "blue")}---'
DASHES = "-------------------------------------"

MSG_ERROR = "Cette commande n'est pas reconnue."

MSG_SAVE = {
    "1": "Sauvegarder le substitut",
}

MSG_SAVED = {
    "1": "Retrouver mes aliments substitués.",
}

MSG_BEST_PRODUCTS = {
    "1": "Chercher un substitut sauvegardé",
    "2": "Faire une recherche d'aliment à remplacer",
}

WALK = True
