class Item:
    def __init__(self, name, price, quanity):
        self.name = name.title()
        self.price = price
        self.quantity = quanity
    def __getattr__(self, attr):
        if attr == 'total':
            return self.price * self.quantity
        else: return attr

item = Item('табуретка', 100, 4)
print(item.name)
print(item.price)
print(item.total)
print(item.color)
