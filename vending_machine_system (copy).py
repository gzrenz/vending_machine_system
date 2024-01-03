
class VendingMachine:
    def __init__(self):
        self.balance = 0
        self.items = {
        "soda" : {"Amount" : 5, "Price": 25}, "popcorn" : {"Amount" : 5, "Price": 20},
        "chips" : {"Amount" : 5, "Price": 15}, "water" : {"Amount" : 5, "Price": 10},
        "fries" : {"Amount" : 5, "Price": 20}, "bread" : {"Amount" : 5, "Price": 15}
        }

    def check_balance(self):
        print(self.balance)

    def cash_in(self, amount):
        self.balance += amount
        print(f"Successfully cashed in amount: {amount}")

    def cash_out(self, amount):
        if amount > self.balance:
            print(f"Sorry, you do not have enough balance to cash out amount {amount}")
        else:
            self.balance -= amount
            print(f"Successfully cashed out amount: {amount}")
    
    def add_items(self, item, amount, price):
        self.items.update({item: {"Amount": amount, "Price" : price}})
        pass

    def remove_items(self, item, amount):
        self.items[item]["Amount"] -= amount
        pass

    def get_amount(self, item):
        return self.items[item]["Amount"]
    
    def get_price(self, item):
        return self.items[item]["Price"]
    
    def set_amount(self, item, amount):
        self.items[item]["Amount"] = amount

    def set_price(self, item, price):
        self.items[item]["Price"] = price

if __name__ == "__main__":
    welcome_string = "Welcome to GX vending machine!"
    print(("*" * len(welcome_string)) + f"\n{welcome_string}\n" + ("*" * len(welcome_string)))
    vendingMachine = VendingMachine()
    total_sales = 0
    while True:
        user_input = input("Options: (0) check balance, (1) cash-in, (2) cash-out, (3) buy-items\n(4) add item/s, (5) remove item/s, (6) check items, (7) exit: ")

        to_del = ""
        for key in vendingMachine.items:
            if vendingMachine.items[key]["Amount"] == 0:
                to_del = key
        try:
            del vendingMachine.items[to_del]
        except KeyError:
            pass
        ######################################################################
        if user_input == "0":
           vendingMachine.check_balance()           
        elif user_input == "1": 
           amount = int(input("Enter amount to be cashed in: "))
           vendingMachine.cash_in(amount)
        elif user_input == "2": 
           amount = int(input("Enter amount to be cashed out: "))
           vendingMachine.cash_out(amount)
        ######################################################################
        elif user_input == "3":
           """buy items"""
           items_bought = {}
           total_price = 0
           num_of_items = int(input("Enter number of different items to be bought: "))
           for x in range(num_of_items):
                item = ""
                while True:
                    item = input("Enter item: ").lower().strip()
                    if item not in vendingMachine.items:
                        print("Item not found, please try again.")
                    else:
                        break
                amount = 0 
                while True:
                    amount = int(input("Enter amount: "))
                    if amount > vendingMachine.get_amount(item):
                        print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount")
                    else:
                        break
                items_bought.update({item: {"Amount": amount, "Price" : vendingMachine.get_price(item)}})
                total_price += amount * vendingMachine.get_price(item)

           if total_price > vendingMachine.balance:
               print("Sorry, you do not have enough balance to purchase the items.")
           else:    
            for key_1 in vendingMachine.items:
                for key_2 in items_bought:
                    if key_1 == key_2:
                        vendingMachine.remove_items(item, items_bought[item]["Amount"])
            print("Items bought: ")
            for item in items_bought:
                    print(item, end=": ")
                    for x in items_bought[item]:
                        print(f"{x} : {items_bought[item][x]} | ", end=" ")
                    print()
            print("Total Price:", total_price)
            vendingMachine.balance -= total_price
            total_sales += total_price
        ######################################################################
        elif user_input == "4":
           """Add Items"""
           num_of_items = int(input("Enter number of items to be added: "))
           for x in range(num_of_items):
               item = input("Enter item: ").lower().strip()
               
               if item in vendingMachine.items:
                   amount = int(input("Enter amount: "))
                   vendingMachine.add_items(item, vendingMachine.get_amount(item) + amount, vendingMachine.get_price())
               else:
                amount = int(input("Enter amount: "))
                price = int(input("Enter price: "))
                vendingMachine.add_items(item, amount, price)
        ######################################################################
        elif user_input == "5":
            """Remove Items"""
            num_of_items = int(input("Enter number of items to be removed: "))
            for x in range(num_of_items):
                item = ""
                while True: 
                    item = input("Enter item to be removed: ").lower().strip()
                    if item not in vendingMachine.items:
                        print("Item not found, please try again.")
                    else: 
                        break
                while True:
                    amount = int(input("Enter amount: "))
                    if amount > vendingMachine.get_amount(item):
                        print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount.")
                    else:
                        vendingMachine.remove_items(item, amount)
                        break
        #####################################################################
        elif user_input == "6":
            for item in vendingMachine.items:
                print(f"{item}".ljust(20, " ").capitalize(), end=": ")
                for x in vendingMachine.items[item]:
                    print(f"{x} : {vendingMachine.items[item][x]} | ", end=" ")
                print()
        #####################################################################
        elif user_input == "7":
            print(f"Total sales: {total_sales}")
            print("Thank you for using the vending machine, good bye!")
            break
        #####################################################################
        else:
            text = "Invalid input. Please try again."
            print("*" * len(text))
            print(text)
            print("*" * len(text))
        
