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
