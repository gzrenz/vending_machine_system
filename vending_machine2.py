import json

def vending_machine(bal, n):
    # Initialize fields
    with open("items.json", "r") as file:
            items = json.load(file)
    
    # print(items)

    total_sales = 0
    name = n
    balance = bal

    # Print welcome 
    welcome_string = "Welcome to GX vending machine!"
    print(("*" * len(welcome_string)) + f"\n{welcome_string}\n" + ("*" * len(welcome_string)))
    
    # Start bending machine loop
    while True:
        text1 = "Options: (0) check balance, (1) cash-in, (2) cash-out, (3) buy-items"
        text2 = "(4) add item/s, (5) remove item/s, (6) check items, (7) exit"
        user_input = input(("*" * len(text1)) + f"\n{text1}" + f"\n{text2}\n" + ("*") * len(text1) + "\n")

        # Delete items if amount is 0
        
        # with open("items.json", "r") as file:
        #     items = json.load(file)
        # to_del = []
        # for key in items:
        #     if items[key]["amount"] == 0:
        #         to_del.append(key)
        # for item in to_del:
        #     items.pop(item)
           
        # newData = json.dumps(items)
        # with open("items.json", "w") as file:
        #     file.write(newData)

        # with open("items.json", "r") as file:
        #     items = json.load(file)

        # Cash in
        if user_input == "0":
           """Check balance"""
           with open("accounts.json") as file:
               data = json.load(file)
               balance = data["accounts"][name]["balance"]
           print(f"₱{balance}") 

        # Cash in           
        elif user_input == "1": 
           try:
                amount = int(input("Enter amount to be cashed in: "))
           except ValueError:
               print("Invalid input. Please try again.")
               continue
           with open("accounts.json", "r") as file:
               data = json.load(file)
               data["accounts"][name]["balance"] += amount

           newData = json.dumps(data, indent=4)
           with open("accounts.json", "w") as file:
               file.write(newData)
               
           print(f"Successfully cashed in ₱{amount}")

        # Cash out
        elif user_input == "2": 
           while True: 
                try:
                    amount = int(input("Enter amount to be cashed out: "))
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue
                if balance < amount:
                    print("Sorry, you do not have enough balance to cash out this amount.")
                else: 
                    with open("accounts.json") as file:
                        data = json.load(file)
                        data["accounts"][name]["balance"] -= amount
                    
                    newData = json.dumps(data, indent=4)
                    with open("accounts.json", "w") as file:
                        file.write(newData)
                    print(f"Successfully cashed out ₱{amount}")
                    break

        # Buy items
        elif user_input == "3":
           with open("items.json", "r") as file:
               data = json.load(file)
           items_stack = []
           items_bought = {}
           total_price = 0
           try: 
            num_of_items = int(input("Enter number of different items to be bought: "))
           except ValueError:
               print("Invalid input. Please try again.")
               continue
           for x in range(num_of_items):
                item = ""
                while True:
                    item = input("Enter item: ").lower().strip()
                    if item not in items:
                        print("Item not found, please try again.")
                    elif item in items_stack:
                        print("Already entered item, try another item!")
                    else:
                        break
                items_stack.append(item)
                amount = 0 
                while True:
                    try: 
                        amount = int(input("Enter amount: "))
                    except ValueError:
                        print("Invalid input. Please try again.")
                        continue
                    if amount > items[item]["amount"]:
                        print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount")
                    else:
                        break
                items_bought.update({item: {"amount": amount, "price" : items[item]["price"]}})
                total_price += amount * items[item]["price"]

           if total_price > balance:
               print("Sorry, you do not have enough balance to purchase the items.")
           else:    
            with open("items.json", "r") as file:
                data = json.load(file)
            for key_1 in items:
                for key_2 in items_bought:
                    if key_1 == key_2:
                        # print("Equal")
                        data[key_1]["amount"] = items[key_1]["amount"] - items_bought[key_2]["amount"]
            newData = json.dumps(data, indent=4)
            with open("items.json", "w") as file:
                file.write(newData)
            print("Items bought: ")
            for item in items_bought:
                    print(item, end=": ")
                    for x in items_bought[item]:
                        print(f"{x} : {items_bought[item][x]} | ", end=" ")
                    print()
            print("Total Price:", total_price)
            with open("accounts.json", "r") as file: 
                data = json.load(file)
                data["accounts"][name]["balance"] -= total_price
            newData = json.dumps(data, indent=4)
            with open("accounts.json", "w") as file:
                file.write(newData)
            total_sales += total_price

        # Add items
        elif user_input == "4":
           try: 
            num_of_items = int(input("Enter number of items to be added: "))
           except ValueError:
               print("Invalid input. Please try again.")
           for x in range(num_of_items):
               item = input("Enter item: ").lower().strip()
               
               if item in items:
                   amount = int(input("Enter amount: "))
                   items[item]["amount"] += amount
                   newData = json.dumps(items, indent=4)
                   with open("items.json", "w") as file:
                       file.write(newData)
               else:
                amount = int(input("Enter amount: "))
                price = int(input("Enter price: "))
                items.update({item : {"amount" : amount, "price" : price}})
                items[item]["amount"] = amount
                items[item]["price"] = price
                newData = json.dump(items, indent=4)
                with open("items.json", "w") as file:
                    file.write(newData)

        # Remove Items
        elif user_input == "5":
            try:
                num_of_items = int(input("Enter number of different items to be removed: "))
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            for x in range(num_of_items):
                item = ""
                while True: 
                    item = input("Enter item to be removed: ").lower().strip()
                    if item not in items:
                        print("Item not found, please try again.")
                    else: 
                        break
                while True:
                    try:
                        amount = int(input("Enter amount: "))
                    except ValueError:
                        print("Invalid input. Please try again")
                        continue
                    if amount > items[item]["amount"]:
                        print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount.")
                    else:
                        items[item]["amount"] -= amount
                        newData = json.dumps(items, indent=4)
                        with open("items.json", "w") as file:
                            file.write(newData)
                        break

        # Show items
        elif user_input == "6":
            with open("items.json", "r") as file:
                items = json.load(file)
            for item in items:
                print(f"{item}".ljust(15, " ").capitalize(), end="- ")
                for x in items[item]:
                    
                    if x == "price":
                        print(f"{x}" + f" : ₱{items[item][x]}".capitalize().ljust(15, " "), end=" ")
                    else:
                        print(f"available" + f" : {items[item][x]}".capitalize().ljust(15, " "), end=" ")
                print()

        # Exit
        elif user_input == "7":
            with open("accounts.json", "r") as file:
                data = json.load(file)
                data["accounts"][name]["balance"] = balance
                newData = json.dumps(data, indent=4)
            
            with open("accounts.json", "w") as file:
                file.write(newData)
            print(f"Total sales : {total_sales}")
            # print("Thank you for using the vending machine, good bye!")
            break
        
        else:
            text = "Invalid input. Please try again."
            print(("*" * len(text)) + f"\n{text}\n" + ("*") * len(text))
            
if __name__ == "__main__":
    # Start accounts loop
    while True:
        try:
            user_input = int(input("(0) login, (1) register, (2) exit: "))
        except ValueError:
            print("Invalid input, please try again.")
            continue
        if user_input == 0:
            username_found = False
            with open("accounts.json", "r") as file:
                data = json.load(file)
                name = input("Enter username: ")
                for n in data["accounts"]:
                    user_found = False
                    # Checks if username is found
                    if name == n:
                        username_found = True
                        while True:
                            # Checks if password is correct
                            password = input("Enter password: ")
                            if password == "x":
                                break
                            elif data["accounts"][name]["password"] != password:
                                print("Wrong password, try again. Press x to exit")
                                continue
                            else:
                                # Enter vending machine system with user balance
                                vending_machine(data["accounts"][name]["balance"], name)
                                break
                if username_found == False:
                    print("Username not found")
        elif user_input == 1:
            with open('accounts.json', 'r') as file:
                data = json.load(file)
                while True:
                    name = input("Enter name: ")
                    with open("accounts.json") as file:
                        data = json.load(file)
                        user_name_already_taken = False
                        for n in data["accounts"]:
                                if n == name:
                                    print("Username already taken")
                                    user_name_already_taken = True
                    if len(name) < 3:
                        print("Username must contain 3 or more characters")
                        continue
                    elif name[0].isdigit():
                        print("Username cannot start with a number")
                        continue
                    
                    elif user_name_already_taken:
                        continue
                    else:
                        break
                while True:
                    password = input("Enter password: ")
                    if len(password) < 8:
                        print("Password must be at least 8 characters")
                        continue
                    break
                data["accounts"][name] = {"balance" : 0, "password" : password}
                newData = json.dumps(data, indent=4)
            with open('accounts.json', 'w') as file:
                file.write(newData)
        elif user_input == 2:
            print("Thank you for using the vending machine, good bye!")
            break
        else:
            print("Invalid input, please try again.")