"""
library_system.py
------------------
A small Library Management System demonstrating all four pillars of
Object-Oriented Programming:

  1. ENCAPSULATION - private/protected attributes accessed only through
     properties and methods (e.g. LibraryItem.__item_id, Person.__person_id,
     Member._borrowed_items).
  2. ABSTRACTION - abstract base classes (LibraryItem, Person) define a
     contract via @abstractmethod without exposing implementation details.
     They cannot be instantiated directly.
  3. INHERITANCE - Book, DVD, and Magazine all inherit from LibraryItem;
     Member and Librarian both inherit from Person.
  4. POLYMORPHISM - calculate_late_fee() and get_details() behave
     differently for each subclass, but are called the same way through a
     common LibraryItem reference (see display_catalog / late fee demo).

Run directly to see a demo:
    python3 library_system.py
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# ABSTRACTION + ENCAPSULATION: LibraryItem is an abstract base class. It
# hides internal state behind properties and forces subclasses to implement
# calculate_late_fee() and get_details().
# ---------------------------------------------------------------------------
class LibraryItem(ABC):
    def __init__(self, title: str, item_id: str):
        self._title = title            # protected attribute
        self.__item_id = item_id       # private attribute (name-mangled)
        self._is_available = True

    @property
    def title(self) -> str:
        return self._title

    @property
    def item_id(self) -> str:
        return self.__item_id

    @property
    def is_available(self) -> bool:
        return self._is_available

    def checkout(self) -> None:
        """Encapsulated state change - external code cannot flip
        _is_available directly without going through this method."""
        if not self._is_available:
            raise ValueError(f"'{self._title}' is already checked out.")
        self._is_available = False

    def return_item(self) -> None:
        self._is_available = True

    @abstractmethod
    def calculate_late_fee(self, days_late: int) -> float:
        """Every item type calculates its own late fee. Must be
        implemented by subclasses (ABSTRACTION)."""
        raise NotImplementedError

    @abstractmethod
    def get_details(self) -> str:
        """Every item type describes itself differently (POLYMORPHISM
        when called through a shared LibraryItem reference)."""
        raise NotImplementedError

    def __str__(self) -> str:
        return self.get_details()


# ---------------------------------------------------------------------------
# INHERITANCE: Book, DVD, Magazine each extend LibraryItem and override the
# abstract methods with their own behaviour (POLYMORPHISM).
# ---------------------------------------------------------------------------
class Book(LibraryItem):
    def __init__(self, title: str, item_id: str, author: str, pages: int):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def calculate_late_fee(self, days_late: int) -> float:
        return round(days_late * 0.25, 2)   # $0.25/day

    def get_details(self) -> str:
        return f"Book: '{self._title}' by {self.author} ({self.pages} pages)"


class DVD(LibraryItem):
    def __init__(self, title: str, item_id: str, runtime_minutes: int):
        super().__init__(title, item_id)
        self.runtime_minutes = runtime_minutes

    def calculate_late_fee(self, days_late: int) -> float:
        return round(days_late * 1.00, 2)   # $1.00/day

    def get_details(self) -> str:
        return f"DVD: '{self._title}' ({self.runtime_minutes} min)"


class Magazine(LibraryItem):
    def __init__(self, title: str, item_id: str, issue_number: int):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def calculate_late_fee(self, days_late: int) -> float:
        return round(days_late * 0.10, 2)   # $0.10/day

    def get_details(self) -> str:
        return f"Magazine: '{self._title}' issue #{self.issue_number}"


# ---------------------------------------------------------------------------
# ABSTRACTION + ENCAPSULATION: Person is an abstract base class for people
# in the system. get_role() is abstract; subclasses supply the behaviour.
# ---------------------------------------------------------------------------
class Person(ABC):
    def __init__(self, name: str, person_id: str):
        self._name = name
        self.__person_id = person_id   # private

    @property
    def name(self) -> str:
        return self._name

    @property
    def person_id(self) -> str:
        return self.__person_id

    @abstractmethod
    def get_role(self) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.get_role()}: {self._name} (ID: {self.person_id})"


# ---------------------------------------------------------------------------
# INHERITANCE: Member and Librarian both extend Person but have different
# responsibilities and data (POLYMORPHISM via get_role()).
# ---------------------------------------------------------------------------
class Member(Person):
    def __init__(self, name: str, person_id: str, max_items: int = 3):
        super().__init__(name, person_id)
        self._max_items = max_items
        self._borrowed_items = []      # encapsulated list

    def get_role(self) -> str:
        return "Member"

    def borrow(self, item: LibraryItem) -> None:
        if len(self._borrowed_items) >= self._max_items:
            raise ValueError(
                f"{self._name} has reached the {self._max_items}-item borrowing limit."
            )
        item.checkout()
        self._borrowed_items.append(item)

    def return_item(self, item: LibraryItem) -> None:
        if item not in self._borrowed_items:
            raise ValueError(f"{self._name} did not borrow '{item.title}'.")
        item.return_item()
        self._borrowed_items.remove(item)

    @property
    def borrowed_items(self) -> list:
        return list(self._borrowed_items)   # return a copy - protects internal state


class Librarian(Person):
    def __init__(self, name: str, person_id: str, employee_number: str):
        super().__init__(name, person_id)
        self.employee_number = employee_number

    def get_role(self) -> str:
        return "Librarian"

    def add_item_to_catalog(self, library: "Library", item: LibraryItem) -> None:
        library.add_item(item)


# ---------------------------------------------------------------------------
# COMPOSITION: Library "has-a" catalog of LibraryItem objects and a list of
# registered Members. It coordinates the other classes without needing to
# know their concrete types (works with any LibraryItem subclass).
# ---------------------------------------------------------------------------
class Library:
    def __init__(self, name: str):
        self.name = name
        self._catalog = []
        self._members = []

    def add_item(self, item: LibraryItem) -> None:
        self._catalog.append(item)

    def register_member(self, member: Member) -> None:
        self._members.append(member)

    def find_item(self, item_id: str):
        for item in self._catalog:
            if item.item_id == item_id:
                return item
        return None

    def display_catalog(self) -> None:
        print(f"--- {self.name} Catalog ---")
        for item in self._catalog:
            status = "Available" if item.is_available else "Checked out"
            # POLYMORPHISM: str(item) calls get_details() - the correct
            # override runs automatically depending on the actual subclass.
            print(f"  {item}  [{status}]")


# ---------------------------------------------------------------------------
# DEMO
# ---------------------------------------------------------------------------
def main():
    library = Library("City Library")

    book = Book("Clean Code", "B001", "Robert Martin", 464)
    dvd = DVD("Inception", "D001", 148)
    magazine = Magazine("National Geographic", "M001", 305)

    for item in (book, dvd, magazine):
        library.add_item(item)

    alice = Member("Alice", "MEM001")
    library.register_member(alice)

    print("=== Initial catalog ===")
    library.display_catalog()

    print("\n=== Alice borrows 'Clean Code' and 'Inception' ===")
    alice.borrow(book)
    alice.borrow(dvd)
    library.display_catalog()

    print("\n=== Late fees after 4 days (POLYMORPHISM: same call, different behaviour) ===")
    for item in (book, dvd, magazine):
        print(f"  {item.title}: ${item.calculate_late_fee(4)}")

    print("\n=== Alice returns 'Clean Code' ===")
    alice.return_item(book)
    library.display_catalog()

    print("\n=== ENCAPSULATION check: can't reach private attrs from outside ===")
    try:
        print(book.__item_id)  # will raise AttributeError - name-mangled
    except AttributeError as e:
        print(f"  Blocked as expected: {e}")

    print("\n=== ABSTRACTION check: can't instantiate an abstract class ===")
    try:
        LibraryItem("Some Title", "X999")
    except TypeError as e:
        print(f"  Blocked as expected: {e}")


if __name__ == "__main__":
    main()