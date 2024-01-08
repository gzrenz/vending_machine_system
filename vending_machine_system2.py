from Item import Item
from vending_machine1 import vending_machine
from accounts import Accounts

"""Initialize fields"""
# Accounts
global accs
accs = Accounts("accounts.json")
# Vending Machine
global vm
vm = vending_machine("items.json")

import json


def vending_machine_system():
    # Initialize fields
    total_sales = 0
    total_items_bought = {}

    # Print welcome
    welcome_string = "Welcome to GX Vending Machine!"
    print(("*" * len(welcome_string)) + f"\n{welcome_string}\n" + ("*" * len(welcome_string)))

    # Start bending machine loop
    while True:
        text1 = "Options: (0) check balance, (1) cash-in, (2) cash-out, (3) buy-items, (4) add items/s"
        text2 = "(5) remove item/s, (6) check items, (7) change password, (8) exit"
        user_input = input(
            ("*" * len(text1)) + f"\n{text1}" + f"\n{text2}\n" + ("*") * len(text1) + "\nPicked Option: ")

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
            print(f"₱{accs.get_account_balance()}")

            # Cash in
        elif user_input == "1":
            try:
                amount = int(input("Enter amount to be cashed in: "))
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            accs.increment_account_balance(amount)
            print(f"Successfully cashed in ₱{amount}")

        # Cash out
        elif user_input == "2":
            while True:
                try:
                    amount = int(input("Enter amount to be cashed out: "))
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue
                if accs.get_account_balance() < amount:
                    print("Sorry, you do not have enough balance to cash out this amount.")
                else:
                    accs.decrement_account_balance(amount)
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
                    if item not in vm.items:
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
                    if amount > vm.items[item]["amount"]:
                        print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount")
                    else:
                        break
                items_bought.update({item: {"amount": amount, "price": vm.items[item]["price"]}})
                total_price += amount * vm.items[item]["price"]

            # Update total items bought
            total_items_bought.update(items_bought)

            if total_price > accs.get_account_balance():
                print("Sorry, you do not have enough balance to purchase the items.")
                continue
            else:
                to_delete = []
                for key_1 in vm.items:
                    for key_2 in items_bought:
                        if key_1 == key_2:
                            # print("Equal")
                            if vm.items[key_1]["amount"] == items_bought[key_2]["amount"]:
                                to_delete.append(key_1)
                            else:
                                vm.items[key_1]["amount"] = vm.items[key_1]["amount"] - items_bought[key_2]["amount"]
                                vm.refresh()
                for item in to_delete:
                    vm.delete_item(item)
                print("Items bought: ")
                for item in items_bought:
                    print(item, end=": ")
                    for x in items_bought[item]:
                        print(f"{x} : {items_bought[item][x]} | ", end=" ")
                    print()
                print("Total Price:", total_price)
                accs.decrement_account_balance(total_price)
                total_sales += total_price

        # Add items
        elif user_input == "4":
            try:
                num_of_items = int(input("Enter number of different items to be added: "))
            except ValueError:
                print("Invalid input. Please try again.")
            for x in range(num_of_items):
                item = input("Enter item: ").lower().strip()

                if item in vm.items:
                    amount = int(input("Enter amount: "))
                    vm.increment_item_num(item, amount)
                else:
                    amount = int(input("Enter amount: "))
                    price = int(input("Enter price: "))
                    vm.add_item(item, amount, price)

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
                    if item not in vm.items:
                        print("Item not found, please try again.")
                    else:
                        break
                while True:
                    try:
                        amount = int(input("Enter amount: "))
                    except ValueError:
                        print("Invalid input. Please try again")
                        continue
                    if amount > vm.items[item]["amount"]:
                        print("Sorry, the amount you entered exceeds the stock. Please enter a lower amount.")
                    elif amount == vm.items[item]["amount"]:
                        vm.delete_item(item)
                        break
                    else:
                        vm.decrement_item_amount(item, amount)
                        break

        # Show items
        elif user_input == "6":
            for item in vm.items:
                print(f"{item}".ljust(20, " ").capitalize(), end="- ")
                for x in vm.items[item]:

                    if x == "price":
                        print(f"{x}" + f" : ₱{vm.items[item][x]}".capitalize().ljust(15, " "), end=" ")
                    else:
                        print(f"available" + f" : {vm.items[item][x]}".capitalize().ljust(15, " "), end=" ")
                print()

        elif user_input == "7":
            while True:
                password = input("Enter password: ")
                if len(password) < 8:
                    print("Password must be at least 8 characters")
                    continue
                else:
                    accs.set_account_password(password)
                break

        # Exit
        elif user_input == "8":
            print(f"Total sales : {total_sales}")
            print("Total items bought: ")
            for item in total_items_bought:
                print(item, end=": ")
                for x in items_bought[item]:
                    print(f"{x} : {items_bought[item][x]} | ", end=" ")
                print()

            # print("Thank you for using the vending machine, good bye!")
            break

        else:
            text = "Invalid input. Please try again."
            print(("*" * len(text)) + f"\n{text}\n" + ("*") * len(text))


"""Main loop"""
if __name__ == "__main__":
    # Start login - signup accounts loop
    while True:
        try:
            user_input = int(input("Options: (0) login, (1) register, (2) exit\nPicked Option: "))
        except ValueError:
            print("Invalid input, please try again.")
            continue
        if user_input == 0:
            username_found = False
            with open("accounts.json", "r") as file:
                data = json.load(file)
                name = input("Enter username: ")
                for n in data:
                    user_found = False
                    # Checks if username is found
                    if name == n:
                        username_found = True
                        while True:
                            # Checks if password is correct
                            password = input("Enter password: ")
                            if password == "x":
                                break
                            elif data[name]["password"] != password:
                                print("Wrong password, try again. Press x to exit")
                                continue
                            else:
                                # Enter vending machine system with user balance
                                accs.set_logged_account(name)
                                vending_machine_system()
                                break
                if username_found == False:
                    print("Username not found")
        elif user_input == 1:
            with open('accounts.json', 'r') as file:
                while True:
                    name = input("Enter name: ")
                    user_name_already_taken = False
                    for n in accs.accounts:
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
                accs.accounts[name] = {"balance": 0, "password": password}
                accs.refresh()
        elif user_input == 2:
            print("Thank you for using the vending machine, good bye!")
            break
        else:
            print("Invalid input, please try again.")