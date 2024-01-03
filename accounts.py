import json

# open file in read-mode
with open('accounts.json', 'r') as file:
    data = json.load(file)
    data["accounts"]["genczar"] = {"balance" : 1000, "password" : "123"}
    newData = json.dumps(data, indent=4)

with open('accounts.json', 'w') as file:
    file.write(newData)
    

