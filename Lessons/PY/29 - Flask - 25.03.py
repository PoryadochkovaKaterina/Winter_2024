# Flask

# Хранение тарелок в виде стопки и забор тарелок из стопки (с начала или конца)
# class Plates:
#     def __init__(self):
#         self.lst = []
#     def Put(self, value):
#         self.lst.append(value)
#     def Get(self):
#         if self.lst:
#             # return self.lst.pop(0)   # взять тарелку с первой
#             return self.lst.pop()   # взять тарелку с последней
#         else:
#             return 'Пусто'
#     def How_many(self):
#         return len(self.lst), self.lst
#
# plat = Plates()
# print(plat.How_many())
# plat.Put('Red')
# plat.Put('Green')
# plat.Put('White')
# plat.Put('Black')
# print(plat.How_many())
# plat.Get()
# plat.Get()
# print(plat.How_many())

# Создание программы сайта
# from flask import Flask
#
# app = Flask(__name__)
# @app.route('/')
#
# def index():
#     return 'Hello world!!! :-) '
#
# if __name__ == "__main__":
#     app.run(debug=True)
