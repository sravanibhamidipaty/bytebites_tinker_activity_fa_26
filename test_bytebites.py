from models import Customer, Item, Menu, Order


def test_order_total_with_multiple_items():
    # An order's total should equal the sum of its items' prices.
    order = Order()
    order.add_item(Item("Spicy Burger", 10.0, "Entrees", 4.5))
    order.add_item(Item("Large Soda", 5.0, "Drinks", 3.8))
    assert order.compute_total() == 15.0


def test_order_total_is_zero_when_empty():
    # An order with no items should total 0, not crash.
    order = Order()
    assert order.compute_total() == 0


def test_filter_by_category_returns_only_matching_items():
    # Filtering "Drinks" should return only the drink items.
    soda = Item("Large Soda", 2.25, "Drinks", 3.9)
    water = Item("Bottled Water", 1.50, "Drinks", 4.2)
    burger = Item("Spicy Burger", 8.50, "Entrees", 4.7)
    menu = Menu([soda, water, burger])

    drinks = menu.filter_by_category("Drinks")

    assert set(drinks) == {soda, water}
    assert burger not in drinks


def test_filter_by_category_with_no_matches_returns_empty():
    # Filtering a category with no items should return an empty list.
    menu = Menu([Item("Spicy Burger", 8.50, "Entrees", 4.7)])
    assert menu.filter_by_category("Desserts") == []


def test_sort_by_popularity_orders_highest_first():
    # Sorting should order items by popularity rating, highest first.
    low = Item("Large Soda", 2.25, "Drinks", 3.9)
    high = Item("Chocolate Cake", 5.00, "Desserts", 4.9)
    mid = Item("Spicy Burger", 8.50, "Entrees", 4.7)
    menu = Menu([low, high, mid])

    ranked = menu.sort_by_popularity()

    assert ranked == [high, mid, low]


def test_customer_verification_requires_purchase_history():
    # A customer is verified only if they have past purchases.
    new_customer = Customer("Ada")
    returning_customer = Customer("Grace", purchase_history=["past order"])
    assert new_customer.verify_user() is False
    assert returning_customer.verify_user() is True
