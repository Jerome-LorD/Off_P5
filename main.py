#!/usr/bin/env python
"""Main application."""
import time

from progressbar import (  # type: ignore
    Bar,
    Percentage,
    ProgressBar,
)

from app import settings as s
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
        print(s.MSG_DB_READY)

        app = Application()
        app.run()

    else:
        print(s.MSG_DB_CREATION)
        pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=8).start()
        for page in range(1, 8):
            down_off = Downloader(page)
            extracted = down_off.extract_data()
            cleaner = OffCleaner()
            cleaned = cleaner.clean(extracted)
            construct = Insert()
            construct.insert_data(cleaned)
            time.sleep(0.01)
            pbar.update(page + 1)

            if page == 7:
                app = Application()
                app.run()
        pbar.finish()


if __name__ == "__main__":
    main()
