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
        """A user is considered real if they have at least one past purchase."""
        return len(self.purchase_history) > 0


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

    def add_item(self, item):
        """Add a single Item to the menu."""
        self.items.append(item)

    def filter_by_category(self, category):
        """Return the items that belong to the given category."""
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        """Return the items sorted by popularity rating, highest first."""
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Order:
    """A single transaction; holds selected items and computes total cost."""

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, item):
        """Add a single Item to the order."""
        self.items.append(item)

    def compute_total(self):
        """Return the total cost of all items in the order."""
        return sum(item.price for item in self.items)


if __name__ == "__main__":
    # Manual test scenario for the ByteBites models.

    # 1. Create a few sample items.
    burger = Item("Spicy Burger", 8.50, "Entrees", 4.7)
    soda = Item("Large Soda", 2.25, "Drinks", 3.9)
    water = Item("Bottled Water", 1.50, "Drinks", 4.2)
    cake = Item("Chocolate Cake", 5.00, "Desserts", 4.9)

    # 2. Build the menu and inspect it.
    menu = Menu()
    for item in (burger, soda, water, cake):
        menu.add_item(item)
    print("Menu has", len(menu.items), "items")

    # 3. Filter by category.
    drinks = menu.filter_by_category("Drinks")
    print("Drinks:", [i.name for i in drinks])
    assert {i.name for i in drinks} == {"Large Soda", "Bottled Water"}

    # 4. Sort by popularity (highest first).
    ranked = menu.sort_by_popularity()
    print("By popularity:", [i.name for i in ranked])
    assert [i.name for i in ranked] == [
        "Chocolate Cake", "Spicy Burger", "Bottled Water", "Large Soda"
    ]

    # 5. Build an order and compute the total.
    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    order.add_item(cake)
    print("Order total:", order.compute_total())
    assert order.compute_total() == 15.75

    # 6. Verify a customer using purchase history.
    new_customer = Customer("Ada")
    returning_customer = Customer("Grace", purchase_history=[order])
    print("New customer verified?", new_customer.verify_user())
    print("Returning customer verified?", returning_customer.verify_user())
    assert new_customer.verify_user() is False
    assert returning_customer.verify_user() is True

    print("All checks passed.")
