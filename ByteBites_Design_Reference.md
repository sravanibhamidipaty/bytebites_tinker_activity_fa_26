# ByteBites Design Reference

This file gives the AI coding assistant consistent context for the ByteBites
backend. Attach it to any design chat so the assistant behaves predictably
instead of re-explaining the same rules each message.

## Project Summary

ByteBites is a food-ordering backend. It models four things: the customers who
order, the food items they browse, the menu that holds those items, and the
order that groups a customer's selected items and computes a total.

## Behavioral Instructions

- **Model only the four candidate classes**: `Customer`, `Item`, `Menu`, and
  `Order`. Do not invent extra classes (no `Payment`, `Database`, `User`,
  `Category` class, etc.) unless the feature request explicitly names them.
- **Match attributes to the feature request** exactly:
  - `Customer`: `name` (String), `purchase_history` (list)
  - `Item`: `name` (String), `price` (float), `category` (String),
    `popularity_rating` (float)
  - `Menu`: `items` (list of Item)
  - `Order`: `items` (list of Item), `total` computed from those items
- **Use Mermaid `classDiagram` syntax** — this is the exact format Project 2
  grades. Output raw Mermaid text in a code block, nothing else.
- **Prefer `-->` (association / "has a")** for relationships. This spec has no
  inheritance, so do not use `--|>` ("is a").
- **Represent behavior as methods** only when the spec implies an action
  (e.g. `Menu.filter_by_category`, `Order.compute_total`,
  `Customer.verify_user`). Do not add speculative CRUD methods.
- **Keep types explicit and consistent** (String, float, list, bool).
- **Keep it simple**: no styling, no notes, no unrelated boilerplate.
- When unsure, favor the wording of the feature request over assumptions, and
  ask a clarifying question rather than guessing.

## Relationships (ground truth)

- A `Customer` places `Order`s.
- An `Order` contains one or more `Item`s and computes the total cost.
- A `Menu` holds the full collection of `Item`s and filters them by category.
