

if __name__ == "__main__":
    items = {
        "soda" : {"amount" : 5, "price": 25}, "popcorn" : {"amount" : 5, "price": 20},
        "chips" : {"amount" : 5, "price": 15}, "water" : {"amount" : 5, "price": 10},
        "fries" : {"amount" : 5, "price": 20}, "bread" : {"amount" : 5, "price": 15}
        }
    balance = 0 
    welcome_string = "Welcome to GX vending machine!"
    print(("*" * len(welcome_string)) + f"\n{welcome_string}\n" + ("*" * len(welcome_string)))
    total_sales = 0
    while True:
        text1 = "Options: (0) check balance, (1) cash-in, (2) cash-out, (3) buy-items"
        text2 = "(4) add item/s, (5) remove item/s, (6) check items, (7) exit"
        user_input = input(("*" * len(text1)) + f"\n{text1}" + f"\n{text2}\n" + ("*") * len(text1) + "\n")

        """Delete item if amount is 0"""
        to_del = []
        for key in items:
            if items[key]["amount"] == 0:
                to_del.append(key)
        for x in to_del:
            del items[x]
        ######################################################################
        if user_input == "0":
           """Check balance"""
           print(f"₱{balance}")           
        elif user_input == "1": 
           """Cash in"""
           try:
                amount = int(input("Enter amount to be cashed in: "))
           except ValueError:
               print("Invalid input. Please try again.")
               continue
           balance += amount
           print(f"Successfully cashed in ₱{amount}")
        elif user_input == "2": 
           """Cash out"""
           
           while True: 
                try:
                    amount = int(input("Enter amount to be cashed out: "))
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue
                if balance < amount:
                    print("Sorry, you do not have enough balance to cash out this amount.")
                else: 
                    balance -= amount
                    print(f"Successfully cashed out ₱{amount}")
                    break
        ######################################################################
        elif user_input == "3":
           """buy items"""
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
            for key_1 in items:
                for key_2 in items_bought:
                    if key_1 == key_2:
                        items[key_1]["amount"] -= items_bought[key_2]["amount"]
            print("Items bought: ")
            for item in items_bought:
                    print(item, end=": ")
                    for x in items_bought[item]:
                        print(f"{x} : {items_bought[item][x]} | ", end=" ")
                    print()
            print("Total Price:", total_price)
            balance -= total_price
            total_sales += total_price
        ######################################################################
        elif user_input == "4":
           """Add Items"""
           try: 
            num_of_items = int(input("Enter number of items to be added: "))
           except ValueError:
               print("Invalid input. Please try again.")
           for x in range(num_of_items):
               item = input("Enter item: ").lower().strip()
               
               if item in items:
                   amount = int(input("Enter amount: "))
                   items[item]["amount"] += amount
               else:
                amount = int(input("Enter amount: "))
                price = int(input("Enter price: "))
                items.update({item : {"amount" : amount, "price" : price}})
        ######################################################################
        elif user_input == "5":
            """Remove Items"""
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
                        break
        #####################################################################
        elif user_input == "6":
            for item in items:
                print(f"{item}".ljust(15, " ").capitalize(), end="- ")
                for x in items[item]:
                    
                    if x == "price":
                        print(f"{x}" + f" : ₱{items[item][x]}".capitalize().ljust(15, " "), end=" ")
                    else:
                        print(f"{x}" + f" : {items[item][x]}".capitalize().ljust(15, " "), end=" ")
                print()
        #####################################################################
        elif user_input == "7":
            print(f"Total sales : {total_sales}")
            print("Thank you for using the vending machine, good bye!")
            break
        #####################################################################
        else:
            text = "Invalid input. Please try again."
            print(("*" * len(text)) + f"\n{text}\n" + ("*") * len(text))
        
