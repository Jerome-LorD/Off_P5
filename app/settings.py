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
    "1": "Rechercher un aliment à remplacer",
    "2": "Rechercher un substitut sauvegardé.",
}

HEADER = f'------{colored("        Pur Beurre App         ", "blue")}------'
DASHES = "-------------------------------------------"
SUB_HEADER = f'-------------- {colored("Voulez vous", "blue")} : --------------\n'

MSG_CHOICE = "\nSaisissez votre choix : "

MSG_ERROR = colored("Cette commande n'est pas reconnue.\n", "red")
ERROR = False

MSG_SAVE = {
    "1": "Sauvegarder le substitut",
    "2": "Retrouver mes aliments substitués.",
}

MSG_SAVED = {
    "1": "Rechercher un autre aliment à remplacer",
    "2": "Retrouver mes aliments substitués.",
}

MSG_BEST_PRODUCTS = {
    "1": "Chercher un substitut sauvegardé",
    "2": "Rechercher un autre aliment à remplacer",
}

BACK_OR_QUIT = f'\n{colored("m", "yellow")} : Revenir au menu\n\
{colored("q", "yellow")} : Quitter\n'
