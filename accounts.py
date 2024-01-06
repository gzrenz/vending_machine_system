import json

class Accounts:
    def __init__(self, accounts_dir):
        self.logged_account = ""
        with open(accounts_dir) as file:
            data = json.load(file)
            self.accounts = {}
            for name in data:
                self.accounts[name] = {"balance" : data[name]["balance"], "password": data[name]["password"]}
    
    def set_logged_account(self, name):
        self.logged_account = name
    def get_account_balance(self):
        return self.accounts[self.logged_account]["balance"]
    def get_account_password(self):
        return self.accounts[self.logged_account]["password"]
    def increment_account_balance(self, balance):
        self.accounts[self.logged_account]["balance"] += balance
        self.refresh()
            
    def decrement_account_balance(self, balance):
        self.accounts[self.logged_account]["balance"] -= balance
        self.refresh()

    def set_account_password(self, password):
        self.accounts[self.logged_account]["password"] = password
        self.refresh()
        

    def print_accounts(self):
        print(self.accounts)

    def refresh(self):
        with open("accounts.json", "w") as file:
            json.dump(self.accounts, file)
        accs = Accounts("accounts.json") 
        self.accounts = accs.accounts

