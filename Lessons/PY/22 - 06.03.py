# lsr = [ [ ] ] * 5
# print(lsr)
#
# lsr[0].append(10)   # добавляет в каждые скобки, т.к. мы один и тот же lst[0], умножили 5 раз
# print(lsr)
# lsr[1].append(10)
# print(lsr)
# lsr.append(30)
# print(lsr)
import pandas as pd

# Задача 21-2
# Создание еще одной таблицы, где клеточки заполнены суммой значений движения движения по маршруту
# 1 1 1
# 2 2 2
# 3 3 3
#
# 1       2(1+1)  3(2+1)
# 3(1+2)  4(2+2)  5(3+2)
# 6(3+3)  7(4+3)  8(5+3)

# JOIN
# a = {'Год':[2001, 2002, 2003], 'Шт':[1, 2, 3], 'A':[100, 200, 300]}
# df = pd.DataFrame(a, index=[2001, 2002, 2003])
# df1 = pd.DataFrame({'Company':['aaa', 'bbb', 'ccc']})
# df2 = df.join(df1)
# print(df2)

# import matplotlib.pyplot as plt
# import pandas as pd
# import random
# df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 8],
#                   'b': [1, 1, 2, 2, 3, 4, 3, 2],
#                   'c': [9, 8, 7, 7, 3, 5, 5, 4]})
# df.index = df['a']
# df[['b', 'c']].plot()
# plt.show()

# df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6, 7, 8],
#                    'b': [1, 5, 2, 6, 3, 7, 8, 5]})
# df.plot.bar()   # barh - горизонтальная диаграмма, bar - вертикальная диаграмма
# plt.show()

# x, y = [], []
# for _ in range(5000):
#     x.append(random.random())
#     y.append(random.random())
# df = pd.DataFrame({'x': x, 'y': y})
# df.plot('x', 'y', kind='scatter')
# plt.show()

# x, y = [], []
# for i in range(-10, 11):
#     x.append(i)
#     y.append(i ** 4)
# df = pd.DataFrame({'cubes': y, 'x': x})
# df.index = df['x']
# df.plot()
# plt.show()

