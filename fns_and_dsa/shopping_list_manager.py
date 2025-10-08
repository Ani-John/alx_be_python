def display_menu():
    print("\n=== Shopping List Manager ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
             # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            if item:  # ensure not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
             # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' has been removed from your shopping list.")
            else:
                print(f"⚠️ '{item}' not found in your shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                i = 1
                for item in shopping_list:
                    print(f"{i}. {item}")
                    i += 1
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':
            print("👋 Goodbye! Have a great shopping day!")
            break

        else:
            print("❌ Invalid choice. Please try again (1-4).")

if __name__ == "__main__":
    main()
    
