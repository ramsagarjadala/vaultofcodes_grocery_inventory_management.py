# Initialize variables to store information about the items in the inventory
item_name = ""
quantity = 0
price = 0.0

# Initialize a list to keep track of the current inventory
inventory = []

# Loop to allow the manager to perform multiple actions in a single session
while True:
    print("\n1. Add new item to inventory")
    print("2. Update item quantity")
    print("3. View current inventory")
    print("4. Remove item from inventory")
    print("5. Exit\n")
    choice = int(input("Enter your choice: "))
    print("")

    if choice == 1:  # Adding new item to the inventory
        item_name = input("Enter the item name: ")
        existing_item = None #checking whether the given item is present ,or not in inventory 
        for item in inventory:
            if item["Item"] == item_name:
                existing_item = item
                break
        if existing_item:
            print(f"\n{item_name} already exists in the inventory.\n if you want to update quantity or price just choose choice 2.")
        else:
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price: ₹"))
            inventory.append({"Item": item_name, "Quantity": quantity, "Price": price})
            print(f"\n{item_name} added to the inventory.")

    elif choice == 2:  # Updating item quantity
        if inventory:
            item_name = input("Enter the item name to update: ")
            found_item = None #checking if the entered item is found or not
            for item in inventory:
                if item["Item"] == item_name:
                    found_item = item
                    break

            if found_item:
                print("\n1. Increase item quantity\n2. Decrease item quantity\n3. Increase item price\n4. Decrease item price\n")
                action = int(input("Choose an option: "))
            
                if action in {1, 2}:  # Update quantity
                    quantity_change = int(input("Enter the quantity change: "))
                    if action == 1:#increasing the quantities 
                        found_item["Quantity"] += quantity_change
                        print(f"Quantity updated to {found_item['Quantity']}.")
                    elif action == 2:#decreasing the quantities
                        if found_item["Quantity"] < quantity_change:
                            print("Insufficient quantity to decrease.")
                        else:
                            found_item["Quantity"] -= quantity_change
                            print(f"Quantity updated to {found_item['Quantity']}.")
                elif action in {3, 4}:  # Update price
                    price_change = float(input("Enter the price change: ₹"))
                    if action == 3:# increase in price
                        found_item["Price"] += price_change
                        print(f"Price updated to ₹{found_item['Price']}.")
                    elif action == 4:#decrease in price  i
                        if found_item["Price"] < price_change:
                            print("Insufficient price to decrease.")
                        else:
                            found_item["Price"] -= price_change
                            print(f"Price updated to ₹{found_item['Price']}.")
                else:
                    print("Invalid choice.")
            else:
                print("The specified item is not available in the inventory.")
        else:
            print("There is no item found in the inventory.")
            
            
    elif choice == 3:  # Viewing current inventory
        print("Current Inventory:")
        if inventory:
            for item in inventory:
                print(f"Item: {item["Item"]}, Quantity: {item["Quantity"]}, Price: ₹{item["Price"]}")
        else:
            print("No items currently available.")

    elif choice == 4:
        if inventory:  # Removing item from the inventory
            remove_item_name = input("Enter the item name to remove: ")
            found_item = None
            for item in inventory:
                if item["Item"] == remove_item_name:
                    found_item = item
                    break

            if found_item:
                inventory.remove(found_item)
                print(f"{remove_item_name} removed from the inventory.")
            else:
                print("Item not found in inventory.")
        else:
            print("No items currently available.")

    elif choice == 5:  # Exiting the program
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
