# class Person:
#     age = 28
#     name = 'Ivan'
# preson = Person
# print(hasattr(preson, 'age'))
# print(hasattr(preson, 'salary'))

# def __init__(self, x, y):
#     self.x = x
#     self.y = y
#
# Point = type('Point', (), {'__init__': __init__})   # добавление метода
#
# def __str__ (self):
#     return str((self.x, self.y))
# Point.__str__ = __str__   # еще один способ добавления метода
#
# lst = [(0, 0), (1, 1), (0, 1),]
# plist = []
# for i in lst:
#     plist.append(Point(i[0], i[1]))   # создание списка из экземпляров класса Point
# for i in plist:
#     # print(i)
#     for j in plist:
#         if (i.x - j.x) ** 2 + (i.y - j.y) ** 2 > 1:
#             print(i, j)

# class Node:
#     def __init__(self, value):
#         self.value = value   # значение узла
#         self.next_node = None   # ссылка на следующий узел
# a = Node(1)   # голова списка, а где конец, мы не знаем
# b = Node(22)   # узел, который надо добавить или голова второго списка
# a.next_node = b
# c = Node(333)
# b.next_node = c
# d = Node(4444)
# c.next_node = d
# e = Node(5)
# d.next_node = e
#
# w = Node('abc')
# w.next_node = a
#
# x = w
# while x.next_node != None:
#     print(x.value)
#     x = x.next_node

# from sqlalchemy.orm import Session, sessionmaker
# from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, SmallInteger
# from sqlalchemy.orm import relationship, declarative_base
#
# engine = create_engine('postgresql+psycopg2://postgres:*****@localhost/postgres')
# session = Session(bind=engine)
#
# Base = declarative_base()
# class Book(Base):   #класс, который соответствует таблице
#     __tablename__ = 'book'
#     book_id = Column(Integer(), primary_key=True)
#     title = Column(String(100), nullable=False)
#     author_id = Column(Integer(), nullable=False)
#     price = Column(Integer(), nullable=False)
#     amount = Column(Integer(), nullable=False)
#
# c1 = Book(book_id=12, title='Иди туда где страшно', author_id=8, price=370, amount=15)
#
# session.add(c1)
# session.commit()


from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, SmallInteger
from sqlalchemy.orm import relationship, declarative_base

engine = create_engine('postgresql+psycopg2://postgres:*****@localhost/postgres')
session = Session(bind=engine)

Base = declarative_base()
class Book(Base):   #класс, который соответствует таблице
    __tablename__ = 'book'
    book_id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    author_id = Column(Integer(), nullable=False)
    price = Column(Integer(), nullable=False)
    amount = Column(Integer(), nullable=False)

q = session.query(Book)
for c in q:
    print(c.book_id, c.title, c.author_id, c.amount, c.price)
print('Количество книг ', session.query(Book).count())
print()
i = session.get(Book, 12)
i.title = 'Кафе на краю земли'   # Изменение значения
session.add(i)

q = session.query(Book)
for c in q:
    print(c.book_id, c.title, c.author_id, c.amount, c.price)
print()

for c in session.query(Book).filter_by(author_id=1):
    print(c.title)
print()
print(session.query(Book).filter_by(author_id=3).first().title)   # фильтр по автор id 3
print()
for i in session.query(Book.title, Book.price, Book.amount).order_by(Book.price).limit(10).all():
    print(f'{i[0]:20} {int(i[1]):5} {i[2]}')

session.commit()