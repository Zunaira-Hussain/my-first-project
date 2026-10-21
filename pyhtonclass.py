"""
CLI Menu Loop - a small item manager.
Data structure: Python list
Algorithms: traversal (List), linear search (Search), removal (Delete)
"""

items = []  # our "notebook": starts empty

while True:  # keeps showing the menu until the user chooses Exit
    print("\n--- Menu ---")
    print("1. Add")
    print("2. List")
    print("3. Count")
    print("4. Search")
    print("5. Delete")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        new_item = input("Enter an item to add: ").strip().lower()
        if new_item == "":
            print("Item cannot be empty.")
        elif new_item in items:
            print(f"'{new_item}' is already in the list.")
        else:
            items.append(new_item)  # O(1): writes at the end
            print(f"Added: {new_item}")

    elif choice == "2":
        if not items:
            print("No items in the list.")
        else:
            for number, name in enumerate(items, start=1):  # traversal: O(n)
                print(f"{number}. {name}")

    elif choice == "3":
        print(f"Total items: {len(items)}")  # O(1)

    elif choice == "4":
        target = input("Search for: ").strip().lower()
        found = False
        checks = 0
        for number, name in enumerate(items, start=1):  # linear search: O(n)
            checks += 1
            if name == target:
                print(f"Found '{target}' at position {number} after {checks} check(s).")
                found = True
                break  # stop early, no need to keep looking
        if not found:
            print(f"'{target}' not found after {checks} check(s).")

    elif choice == "5":
        target = input("Enter item to delete: ").strip().lower()
        if target in items:
            items.remove(target)
            print(f"Deleted: {target}")
        else:
            print(f"'{target}' not found.")

    elif choice == "6":
        print("Goodbye!")
        break  # leaves the while loop, so the program ends

    else:
        print("Invalid choice. Please try again.")