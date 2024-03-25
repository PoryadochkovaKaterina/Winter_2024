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

# class Item:
#     def __init__(self, name, price, quantity):
#         self._name = name
#         self.price = price
#         self.quantity = quantity
#
#     @property
#     def total(self):
#         return self.price * self.quantity
#
#     @property
#     def name(self):
#         return self._name.title()
#
# d = Item('табуретка', 15, 3)
# print(d.total, d.name)

# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def __getattribute__(self, attrname):
#         if attrname == 'name':
#             return object.__getattribute__(self, attrname).title()
#         else:
#             return object.__getattribute__(self, attrname)
#
#     def __getattr__(self, attrname):
#         if attrname == 'total':
#             return self.price * self.quantity
#         else: raise AttributeError
#
#     @property
#     def color(self):
#         return 'Red'
#
# d = Item('табуретка', 15, 3)
# print(d.total, d.name)