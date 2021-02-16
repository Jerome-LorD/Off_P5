#!/usr/bin/env python
"""Main application."""
from app.app import Application
from app.models.create_off import Create
from app.models.insert_off import Downloader, Insert, OffCleaner


def main():
    """Entry point app."""
    create = Create()
    create.create_user()
    create.create_db()
    insert = Insert()

    if insert.is_data_in_db():
        # Check if the database contains at least 3000 entries.
        print("La base de donnée est prête.\n")

        app = Application()
        app.run()

    else:
        print("Creation de la db... Patientez le temps de la procédure.")
        for page in range(1, 8):
            down_off = Downloader(page)
            extracted = down_off.extract_data()
            cleaner = OffCleaner()
            cleaned = cleaner.clean(extracted)
            construct = Insert()
            construct.insert_data(cleaned)


if __name__ == "__main__":
    main()
