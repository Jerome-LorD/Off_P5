#!/usr/bin/env python
"""Select detail product module."""

from app.views.main_page import View


class SelectDetailTst:
    """Select detail."""

    def __init__(self, instance):
        """Init."""
        self.view: View = View()
        self.instance = instance[0]

    def display(self):
        """Display."""
        self.view.display_detail_tst(instance=self.instance)

    def get_input(self):
        """Get the input."""
        pass

    def update(self, command: str):
        """Update."""
        return self.instance, "substitute"
