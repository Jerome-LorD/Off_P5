#!/usr/bin/env python
"""Contains all p5 constants."""
from colorama import init
from termcolor import colored


init(autoreset=True)


def justify(text="", lenght: int = 0):
    """Justify the text."""
    return "{:>{}}".format(text, (len(text) + lenght))


def centerize(text="", lenght: int = 0):
    """Centerize the text."""
    return "{: ^{}}".format(text, (len(text) + lenght))


DB_NAME = "offdb"
SQL_FILE = "offdb_p5.sql"

# Manage the header and footer lenght
CHAR_LENGHT = 50

APP_TITLE = centerize("Pur Beurre - App", CHAR_LENGHT)

QUIT_APP = "quit-app"
NEXT_PAGE = "next-page"
PREVIOUS_PAGE = "previous-page"
BACK_TO_MENU = "back-to-menu"

ONE = justify("1", 1)
TWO = justify("2", 1)

MSG_DB_CREATION = "\nCreation de la db... Patientez le temps de la procédure.\n"
MSG_DB_READY = "La base de donnée est prête.\n"
MSG_CHOICE = f'\n\n{justify("Saisissez votre choix : ", 3)}'
MSG_SAVE = {
    f"{ONE}": "Sauvegarder le substitut",
    f"{TWO}": "Retrouver mes aliments substitués.",
}

MSG_SAVED = {
    f"{ONE}": "Rechercher un autre aliment à remplacer",
    f"{TWO}": "Retrouver mes aliments substitués.",
}
MSG_ERROR = colored(justify("Cette commande n'est pas reconnue.\n", 3), "red")

NEXT_PREVIOUS_PAGE = f"{colored(justify('p', 1), 'yellow')} : Page précédente |\
 {colored('n', 'yellow')} : Page suivante\n"

SELECT_CATEGORY = colored(justify("Selectionnez une catégorie :", 2), "cyan")
SELECT_PRODUCT = colored(justify("Sélectionnez un produit :", 2), "cyan")
SUBSTITUTED_DETAIL = colored(justify("Détail du produit sélectionné", 2), "cyan")
SUBSTITUTE_DETAIL = colored(justify("Détail du produit de substitution", 2), "cyan")
CONFIRM_TITLE = justify(
    "Confirmation d'enregistrement du couple de produits sélectionnés :", 3
)
CONFIRMATION = colored(
    justify("Les produits ont bien été enregistrés dans vos favoris.", 4), "green"
)
SAVED_PRODUCTS = justify("Les produits que vous avez enregistré :", 2)

NO_SUBSTITUTE = colored(
    justify(
        "Il n'y a pas de produit avec un meilleur nutriscore dans cette catégorie.", 3
    ),
    "red",
)
BEST_CHOICE = justify(
    f"Très bon choix, le nutriscore est le meilleur possible.\
 {colored('Pas de substitut', 'red')}.",
    3,
)
YOU_HAVE_SELECTED = colored(justify("Vous avez sélectionné", 3), "cyan")

PRODUCT = justify("Produit", 1)
BRAND = justify("Marque", 1)
STORES = justify("Magasins", 1)
URL = justify("URL", 1)
NUTRISCORE = justify("nutriscore", 1)

MENU_CHOICES = {
    f"{ONE}": "Rechercher un aliment à remplacer",
    f"{TWO}": "Rechercher un substitut sauvegardé.",
}

ANSI_LEN = len(colored("", "blue", attrs=["bold"]))
COMMANDS = centerize("Autres commandes", CHAR_LENGHT)

DSH = "-"

HEADER = justify(f"{DSH * 6}{colored(APP_TITLE, 'blue', attrs=['bold'])}{DSH * 6}", 1)
DASHES = justify(DSH * (len(HEADER) - ANSI_LEN - 1), 1)

CR = "\n" * 4  # carriage return
SUB_HEADER = justify(
    f"{DSH * 6}{colored(COMMANDS, 'blue', attrs=['bold'])}{DSH * 6}\n", 1
)
BACK_OR_QUIT = f'{colored(justify("m", 1), "yellow")} : Revenir au menu\n\
{colored(justify("q", 1), "yellow")} : Quitter\n'

ERROR = False
