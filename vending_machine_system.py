
class VendingMachine:
    def __init__(self):
        self.balance = 0
        self.items = {
        "Soda" : {"Amount" : 5, "Price": 25}, "Popcorn" : {"Amount" : 5, "Price": 20},
        "Chips" : {"Amount" : 5, "Price": 15}, "Water" : {"Amount" : 5, "Price": 10},
        "Fries" : {"Amount" : 5, "Price": 20}, "Bread" : {"Amount" : 5, "Price": 15}
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

if __name__ == "__main__":
    welcome_string = "Welcome to GX vending machine!"
    print(("*" * len(welcome_string)) + f"\n{welcome_string}\n" + ("*" * len(welcome_string)))
    vendingMachine = VendingMachine()
    while True:
        user_input = input("Options: (0) check balance, (1) cash-in, (2) cash-out, (3) buy-items\n(4) add item/s, (5) remove item/s, (6) check items, (7) exit: ")
        
        if user_input == "0":
           vendingMachine.check_balance()           
        elif user_input == "1": 
           amount = int(input("Enter amount to be cashed in: "))
           vendingMachine.cash_in(amount)
        elif user_input == "2": 
           amount = int(input("Enter amount to be cashed out: "))
           vendingMachine.cash_out(amount)


        elif user_input == "3":
           """buy items"""
           items_bought = {}
           total_price = 0
           num_of_items = int(input("Enter number of different items to be bought: "))
           for x in range(num_of_items):
                item = input("Enter item: ")
                amount = 0 
                while True:
                    amount = int(input("Enter amount: "))
                    if amount > vendingMachine.items[item]["Amount"]:
                        print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount")
                    else:
                        vendingMachine.items[item]["Amount"] -= amount
                        break
                items_bought.update({item: {"Amount": amount, "Price" : vendingMachine.items[item]["Price"]}})
                total_price += amount * vendingMachine.items[item]["Price"]

           if total_price > vendingMachine.balance:
               print("Sorry, you do not have enough balance to purchase the items.")
           else:    
            print("Items bought: ")
            for type in items_bought:
                    print(type, end=": ")
                    for x in items_bought[type]:
                        print(f"{x} : {items_bought[type][x]} | ", end=" ")
                    print()
            print("Total Price:", total_price)

        elif user_input == "4":
           """Add Items"""
           num_of_items = int(input("Enter number of items to be added: "))
           for x in range(num_of_items):
               item = input("Enter item: ")
               
               if item in vendingMachine.items:
                   amount = int(input("Enter amount: "))
                   vendingMachine.items[item]["Amount"] += amount
               else:
                amount = int(input("Enter amount: "))
                price = int(input("Enter price: "))
                vendingMachine.items.update({item: {"Amount": amount, "Price" : price}})
        elif user_input == "5":
            """Remove Items"""
            num_of_items = int(input("Enter number of items to be removed: "))
            for x in range(num_of_items):
                item = input("Enter item to be removed: ")
                while True:
                    amount = int(input("Enter amount: "))
                    if amount > vendingMachine.items["Amount"]:
                        print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount.")
                    else:
                        vendingMachine.items[type]["Amount"] -= amount
                        break
        elif user_input == "6":
            for type in vendingMachine.items:
                print(type, end=": ")
                for x in vendingMachine.items[type]:
                    print(f"{x} : {vendingMachine.items[type][x]} | ", end=" ")
                print()
        elif user_input == "7":
            print("Thank you for using the vending machine, good bye!")
            break
        else:
            print("Invalid input. Please try again.")
        
