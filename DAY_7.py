# Shopping List App

# Step 1: Innitialise an empty shopping list
shopping_list = ["Egg", "Milk", "Bread", "Butter"]

# Step 2: Define the main menu
def show_menu():
    print("\n--- Shopping List Menu ---")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear list")
    print("5. Exit")

def add_items_to_list(shopping_list, *items):
    shopping_list.extend(items)
    for item in items:
        print(f"{item} has been added to the shopping list.")

# Step 3: Main program Loop
while True:
    show_menu()
    choice = input("Ente your choice (1-5): ")

    if choice == "1":
        print("\n--- Shipping List ---")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}, {item}")
        break
            
    elif choice == "2":
        # item = input("Enter the item to add: ")
        # shopping_list.append(item)
        items = input("Enter the items to add (separate by commas): ")
        # Split the input string by commas, strip spaces, and add each item to the list
        item_list = [item.strip() for item in items.split(',')]
        add_items_to_list(shopping_list, *item_list)
        print(f"Items {', '.join(item_list)} have been added to the shopping list.")
        print(shopping_list)
        break

    elif choice == "3":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shoping_list.")
            print(shopping_list)

        else:
            print(f"{item} is not in the shipping list.")
        break
        
        
    elif choice == "4":
        shopping_list.clear()
        print("The shopping list has been cleared.")
        print(shopping_list)
        break

    elif choice == "5":
        print("Goodbye! Happy Shopping!")
        break
    else:
        print("Invalid choice. Please try again.")


