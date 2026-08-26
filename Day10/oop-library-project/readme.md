# Library Management System — OOP Pillars Demo

A small, self-contained Python project modeling a library, built specifically
to showcase all four pillars of Object-Oriented Programming in one place.

## Run it

```bash
python3 library_system.py
```

No dependencies — pure Python standard library (`abc`).

## Class overview

```
LibraryItem (ABC)              Person (ABC)
   ├── Book                       ├── Member
   ├── DVD                        └── Librarian
   └── Magazine

Library  → composed of many LibraryItem + Member objects
```

## Where each pillar lives

### 1. Encapsulation
- `LibraryItem.__item_id` and `Person.__person_id` are private (double
  underscore → name-mangled), only reachable via the `item_id` / `person_id`
  read-only `@property`.
- `LibraryItem._is_available` can only be changed through `checkout()` /
  `return_item()` — never set directly from outside the class.
- `Member._borrowed_items` is protected, and `Member.borrowed_items` returns
  a **copy** of the list so external code can't mutate the member's internal
  state.

### 2. Abstraction
- `LibraryItem` and `Person` are `ABC` subclasses with `@abstractmethod`
  methods (`calculate_late_fee`, `get_details`, `get_role`). They define
  *what* a subclass must do, not *how*.
- Trying to instantiate `LibraryItem(...)` or `Person(...)` directly raises
  a `TypeError` — proven in the demo output.

### 3. Inheritance
- `Book`, `DVD`, and `Magazine` all inherit from `LibraryItem`, reusing
  `checkout()`, `return_item()`, and the `title`/`item_id`/`is_available`
  properties.
- `Member` and `Librarian` both inherit from `Person`, reusing `name`,
  `person_id`, and `__str__`.

### 4. Polymorphism
- `calculate_late_fee()` and `get_details()` are overridden differently in
  `Book`, `DVD`, and `Magazine`. The demo loops over a list of mixed item
  types and calls `item.calculate_late_fee(4)` on each — the correct
  version runs automatically depending on the actual object type.
- `Library.display_catalog()` calls `str(item)` (which calls
  `get_details()`) on every item without knowing or caring whether it's a
  `Book`, `DVD`, or `Magazine`.

## What the demo script does

1. Creates a `Library`, adds a `Book`, a `DVD`, and a `Magazine`.
2. Registers a `Member` ("Alice") and has her borrow two items.
3. Prints the catalog before/after borrowing to show state changes.
4. Computes late fees for all three item types with one polymorphic loop.
5. Returns an item and shows the catalog update.
6. Proves encapsulation by trying (and failing) to read a private attribute.
7. Proves abstraction by trying (and failing) to instantiate `LibraryItem`
   directly.

## Extending it

Ideas if you want to build on this:
- Add an `EBook` class with its own late-fee rule (e.g. no fee — it just
  expires) to see inheritance/polymorphism in action again.
- Add a `Library.overdue_report(days_late)` method that loops over all
  currently checked-out items and totals late fees polymorphically.
- Add exception classes (`ItemNotAvailableError`, `BorrowLimitError`)
  instead of generic `ValueError` for more realistic error handling.