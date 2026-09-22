# ByteBites backend models
#
# Four classes model this system, based on bytebites_spec.md and
# bytebites_design.mmd:
#
#   Customer - a real user; stores their name and past purchase history,
#              used to verify they are a real user.
#   Item     - a single food item; stores name, price, category, and
#              popularity rating.
#   Menu     - the full collection of items; holds all items and filters
#              them by category (e.g. "Drinks", "Desserts").
#   Order    - a single transaction; stores the selected items and
#              computes the total cost.


class Customer:
    """A real user; tracks their name and past purchase history."""

    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def verify_user(self):
        """Return True if the customer is a real user."""
        pass


class Item:
    """A single food item on the menu."""

    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """The full collection of items; supports filtering by category."""

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def filter_by_category(self, category):
        """Return the items that belong to the given category."""
        pass


class Order:
    """A single transaction; holds selected items and computes total cost."""

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def compute_total(self):
        """Return the total cost of all items in the order."""
        pass
