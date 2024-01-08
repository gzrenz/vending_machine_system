from Item import Item
class Linked_List:
    def __init__(self):
        self.len = 0
        self.start = Item(None, None, None, None, None, None)
        self.end = Item(None, None, None, None, self.start, None)
        self.start = Item(None, None, None, None, None, self.end)
    def return_array(self):
        array_list = []
        item = self.start
        while item.next != None:
            array_list.append([[item.next.index, item.next.name, item.next.price, item.next.amount]])
            item = item.next
        return array_list
    def add_item(self, name, price, amount):
        item = Item(self.len, name, price, amount, self.end.prev, self.end)
        self.end.prev = item
        self.end.prev.prev.next = item

    def print(self):
        item = self.start
        while item.next != None:
            print(item.next.name)
            item = item.next
if __name__ == "__main__":
    l = Linked_List()
    l.add_item("soda", 20, 5)
    l.add_item("popcorn", 20, 5)
    l.print()
