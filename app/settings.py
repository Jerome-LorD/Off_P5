#!/usr/bin/env python
"""Contains all p5 constants."""

DB_NAME = "offdb"
SQL_FILE = "app/sql/offdb_p5.sql"

# Manage the header and footer lenght
CHAR_LENGHT = 50

APP_TITLE = "Pur Beurre - App"

QUIT_APP = "quit-app"
NEXT_PAGE = "next-page"
PREVIOUS_PAGE = "previous-page"
BACK_TO_MENU = "back-to-menu"

MSG_DB_CREATION = "\nCreation de la db... Patientez le temps de la procédure.\n"
MSG_DB_READY = "La base de donnée est prête.\n"
MSG_CHOICE = "Saisissez votre choix : "

SAVE_ITEM = "Sauvegarder le substitut"
OTHER_ITEM = "Rechercher un autre aliment à remplacer"
DELETE_ITEM = "Supprimer le favori"

MSG_ERROR = "Cette commande n'est pas reconnue.\n"

SELECT_CATEGORY = "Selectionnez une catégorie :"
SELECT_PRODUCT = "Sélectionnez un produit :"
SUBSTITUTED_DETAIL = "Détail du produit sélectionné"
SUBSTITUTE_DETAIL = "Détail du produit de substitution"
CONFIRM_TITLE = "Confirmation d'enregistrement du couple de produits sélectionnés :"
DEL_CONFIRM = "Les produits sont supprimés de vos favoris."
SAVE_CONFIRM = "Les produits ont bien été enregistrés dans vos favoris."
SAVED_PRODUCTS = "Les produits que vous avez enregistré :"
DEL_ALERT = "Attention, cette suppression sera définitive."
NO_SUBSTITUTE = "Il n'y a pas de produit similaire avec un meilleur nutriscore\
 dans cette catégorie."

YOU_HAVE_SELECTED = "Vous avez sélectionné"

PRODUCT = "Produit"
BRAND = "Marque"
STORES = "Magasins"
URL = "URL"
NUTRISCORE = "nutriscore"

OTHER_COMMANDS = "Autres commandes"

DSH = "-"
CR = "\n" * 4  # carriage return

BACK = "Revenir au menu"
QUIT = "Quitter"
ERROR = False
