import json
class vending_machine:
    def __init__(self, items_dir):
        with open(items_dir, "r") as file:
            data = json.load(file)
            self.items = {}
            for name in data:
                self.items[name] = {"amount": data[name]["amount"], "price" : data[name]["price"]}
    
    def get_item_price(self, name):
        return self.items[name]["price"]
    def get_item_amount(self, name):
        return self.items[name]["amount"]
    def set_item_price(self, name, price):
        self.items[name]["price"] = price
        self.refresh()
    def decrement_item_amount(self, name, amount):
        self.items[name]["amount"] -= amount
        self.refresh()
    def delete_item(self, name):
        del self.items[name]
        self.refresh()
    def add_item(self, name, amount, price):
        self.items.update({name : {"amount": amount, "price": price}})
        self.refresh()
    def increment_item_num(self, name, amount):
        self.items[name]["amount"] += amount
        self.refresh()

    def refresh(self):
        with open("items.json", "w") as file:
            json.dump(self.items, file)
        vm = vending_machine("items.json") 
        self.items = vm.items
    

# def vending_machine(bal, n):
#     # Initialize fields
#     items = {
#         "soda" : {"amount" : 5, "price": 25}, "popcorn" : {"amount" : 5, "price": 20},
#         "chips" : {"amount" : 5, "price": 15}, "water" : {"amount" : 5, "price": 10},
#         "fries" : {"amount" : 5, "price": 20}, "bread" : {"amount" : 5, "price": 15}
#         }
#     total_sales = 0
#     name = n
#     balance = bal

#     # Print welcome 
#     welcome_string = "Welcome to GX vending machine!"
#     print(("*" * len(welcome_string)) + f"\n{welcome_string}\n" + ("*" * len(welcome_string)))
    
#     # Start loop
#     while True:
#         text1 = "Options: (0) check balance, (1) cash-in, (2) cash-out, (3) buy-items"
#         text2 = "(4) add item/s, (5) remove item/s, (6) check items, (7) exit"
#         user_input = input(("*" * len(text1)) + f"\n{text1}" + f"\n{text2}\n" + ("*") * len(text1) + "\n")

#         # Delete items if amount is 0
#         while True:
#             to_del = ""
#             for key in items:
#                 if items[key]["amount"] == 0:
#                     to_del = key
#             try:
#                 del items[to_del]
#                 continue
#             except KeyError:
#                 pass
#             break

#         # Cash in
#         if user_input == "0":
#            """Check balance"""
#            print(f"₱{balance}")           
#         elif user_input == "1": 
#            """Cash in"""
#            try:
#                 amount = int(input("Enter amount to be cashed in: "))
#            except ValueError:
#                print("Invalid input. Please try again.")
#                continue
#            balance += amount
#            print(f"Successfully cashed in ₱{amount}")

#         # Cash out
#         elif user_input == "2": 
#            while True: 
#                 try:
#                     amount = int(input("Enter amount to be cashed out: "))
#                 except ValueError:
#                     print("Invalid input. Please try again.")
#                     continue
#                 if balance < amount:
#                     print("Sorry, you do not have enough balance to cash out this amount.")
#                 else: 
#                     balance -= amount
#                     print(f"Successfully cashed out ₱{amount}")
#                     break

#         # Buy items
#         elif user_input == "3":
#            items_stack = []
#            items_bought = {}
#            total_price = 0
#            try: 
#             num_of_items = int(input("Enter number of different items to be bought: "))
#            except ValueError:
#                print("Invalid input. Please try again.")
#                continue
#            for x in range(num_of_items):
#                 item = ""
#                 while True:
#                     item = input("Enter item: ").lower().strip()
#                     if item not in items:
#                         print("Item not found, please try again.")
#                     elif item in items_stack:
#                         print("Already entered item, try another item!")
#                     else:
#                         break
#                 items_stack.append(item)
#                 amount = 0 
#                 while True:
#                     try: 
#                         amount = int(input("Enter amount: "))
#                     except ValueError:
#                         print("Invalid input. Please try again.")
#                         continue
#                     if amount > items[item]["amount"]:
#                         print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount")
#                     else:
#                         break
#                 items_bought.update({item: {"amount": amount, "price" : items[item]["price"]}})
#                 total_price += amount * items[item]["price"]

#            if total_price > balance:
#                print("Sorry, you do not have enough balance to purchase the items.")
#            else:    
#             for key_1 in items:
#                 for key_2 in items_bought:
#                     if key_1 == key_2:
#                         items[key_1]["amount"] -= items_bought[key_2]["amount"]
#             print("Items bought: ")
#             for item in items_bought:
#                     print(item, end=": ")
#                     for x in items_bought[item]:
#                         print(f"{x} : {items_bought[item][x]} | ", end=" ")
#                     print()
#             print("Total Price:", total_price)
#             balance -= total_price
#             total_sales += total_price

#         # Add items
#         elif user_input == "4":
#            try: 
#             num_of_items = int(input("Enter number of items to be added: "))
#            except ValueError:
#                print("Invalid input. Please try again.")
#            for x in range(num_of_items):
#                item = input("Enter item: ").lower().strip()
               
#                if item in items:
#                    amount = int(input("Enter amount: "))
#                    items[item]["amount"] += amount
#                else:
#                 amount = int(input("Enter amount: "))
#                 price = int(input("Enter price: "))
#                 items.update({item : {"amount" : amount, "price" : price}})

#         # Remove Items
#         elif user_input == "5":
#             try:
#                 num_of_items = int(input("Enter number of different items to be removed: "))
#             except ValueError:
#                 print("Invalid input. Please try again.")
#                 continue
#             for x in range(num_of_items):
#                 item = ""
#                 while True: 
#                     item = input("Enter item to be removed: ").lower().strip()
#                     if item not in items:
#                         print("Item not found, please try again.")
#                     else: 
#                         break
#                 while True:
#                     try:
#                         amount = int(input("Enter amount: "))
#                     except ValueError:
#                         print("Invalid input. Please try again")
#                         continue
#                     if amount > items[item]["amount"]:
#                         print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount.")
#                     else:
#                         items[item]["amount"] -= amount
#                         break

#         # Show items
#         elif user_input == "6":
#             for item in items:
#                 print(f"{item}".ljust(15, " ").capitalize(), end="- ")
#                 for x in items[item]:
                    
#                     if x == "price":
#                         print(f"{x}" + f" : ₱{items[item][x]}".capitalize().ljust(15, " "), end=" ")
#                     else:
#                         print(f"{x}" + f" : {items[item][x]}".capitalize().ljust(15, " "), end=" ")
#                 print()

#         # Exit
#         elif user_input == "7":
#             with open("accounts.json", "r") as file:
#                 data = json.load(file)
#                 data["accounts"][name]["balance"] = balance
#                 newData = json.dumps(data, indent=4)
            
#             with open("accounts.json", "w") as file:
#                 file.write(newData)
#             print(f"Total sales : {total_sales}")
#             print("Thank you for using the vending machine, good bye!")
#             break
        
#         else:
#             text = "Invalid input. Please try again."
#             print(("*" * len(text)) + f"\n{text}\n" + ("*") * len(text))
        


# if __name__ == "__main__":
#     while True:
#         try:
#             user_input = int(input("(0) login, (1) register: "))
#         except ValueError:
#             print("Invalid input, please try again.")
#             continue
#         if user_input == 0:
#             username_found = False
#             with open("accounts.json", "r") as file:
#                 data = json.load(file)
#                 name = input("Enter username: ")
#                 for n in data["accounts"]:
#                     user_found = False
#                     # Checks if username is found
#                     if name == n:
#                         username_found = True
#                         while True:
#                             # Checks if password is correct
#                             password = input("Enter password: ")
#                             if password == "x":
#                                 break
#                             elif data["accounts"][name]["password"] != password:
#                                 print("Wrong password, try again. Press x to exit")
#                                 continue
#                             else:
#                                 # Enter vending machine system with user balance
#                                 vending_machine(data["accounts"][name]["balance"], name)
#                                 break
#                 if username_found == False:
#                     print("Username not found")
#         elif user_input == 1:
#             with open('accounts.json', 'r') as file:
#                 data = json.load(file)
#                 while True:
#                     name = input("Enter name: ")
#                     with open("accounts.json") as file:
#                         data = json.load(file)
#                         user_name_already_taken = False
#                         for n in data["accounts"]:
#                                 if n == name:
#                                     print("Username already taken")
#                                     user_name_already_taken = True
#                     if len(name) < 3:
#                         print("Username must contain 3 or more characters")
#                         continue
#                     elif name[0].isdigit():
#                         print("Username cannot start with a number")
#                         continue
                    
#                     elif user_name_already_taken:
#                         continue
#                     else:
#                         break
#                 while True:
#                     password = input("Enter password: ")
#                     if len(password) < 8:
#                         print("Password must be at least 8 characters")
#                         continue
#                     break
#                 data["accounts"][name] = {"balance" : 0, "password" : password}
#                 newData = json.dumps(data, indent=4)
#             with open('accounts.json', 'w') as file:
#                 file.write(newData)
#         else:
#             print("Invalid input, please try again.")