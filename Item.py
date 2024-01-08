class Item:
    def __init__(self, index, name, price, amount, prev, next):
        self.index = index
        self.name = name
        self.price = price
        self.amount = amount
        self.next = next
        self.prev = prev