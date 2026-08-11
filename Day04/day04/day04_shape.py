# =======================================================
# Pattern Programs - All in One File
# =======================================================


def star_triangle(rows=4):
    """Prints a decreasing star triangle."""
    print("\n--- Decreasing Star Triangle ---")
    for i in range(rows, 0, -1):        # start at 'rows', count down to 1
        print("* " * i)


def letter_triangle(rows=4):
    """Prints an increasing left-aligned 'A' triangle."""
    print("\n--- Increasing A Triangle ---")
    for i in range(1, rows + 1):        # 1, 2, 3, 4
        print("A " * i)


def letter_pyramid(rows=4):
    """Prints a centered 'A' pyramid."""
    print("\n--- Centered A Pyramid ---")
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)       # left padding to center it
        letters = "A " * i
        print(spaces + letters)


def number_triangle(rows=4):
    """Prints a number triangle: 1 / 2 3 / 4 5 6 / 7 8 9 10."""
    print("\n--- Number Triangle ---")
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()   # move to next line after each row




# ----- Main Program -----
star_triangle()
letter_triangle()
letter_pyramid()
number_triangle()