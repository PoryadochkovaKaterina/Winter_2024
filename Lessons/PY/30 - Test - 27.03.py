# lst = ['hello']
# lst.extend('world')
# print(lst[1])
# print(lst)

# a = {'B': 5, 'A': 9, 'C': 7}
# res = sorted(a)
# print(res)

# ТЕСТИРОВАНИЯ ПРОГРАММНОГО КОДА
# import unittest
# def cube_area(side):
#     return 6 * side ** 2
# print(cube_area(3))
# print(cube_area(3.0))

# side_lst = [10, 0, -3, True, 'five',  [1]]
# for side in side_lst:
#     res = cube_area(side)
#     print(res)   # Вылетает на 'five', но при этом работает на -3 и 0


# import unittest
# def cube_area(side):
#     # функция вычисляет площадь поверхности куба
#     if side == 0: raise ValueError('Передано нулевое значение')
#     if type(side) == bool: raise TypeError
#     if not isinstance(side, (int, float)): raise TypeError
#     return 6 * side ** 2
# class TestCubeAtea(unittest.TestCase):
#     # метод начинается с префикса test_.
#     def test_cube_area(self):
#         self.assertEqual(cube_area(3), 54)  # ОК
#         # self.assertEqual(cube_area(4), 54)   # Failed
#         # self.assertEqual(cube_area(0), 0)   # ОК, хотя площадь от 0 не считается
#     def test_value(self):
#         self.assertRaises(ValueError, cube_area, 0)   # т.к площади от 0 не может быть, то пишем исключение набора
#         # если не прописать исключение в саму функцию, то тест пройден не будет
#     def test_type(self):
#         self.assertRaises(TypeError, cube_area, True)
#         self.assertRaises(TypeError, cube_area, [0])
#         self.assertRaises(TypeError, cube_area, {})
#         self.assertRaises(TypeError, cube_area, (1, 2))
#
# if __name__ == '__main__':
#     unittest.main()   # запуск программы

# Тестирование программы 29-1
# import unittest
# def one(spisok):
#     if not isinstance(spisok, list): raise TypeError
#     if len(spisok) <= 2: raise ValueError
#     for i in spisok:
#         if not isinstance(i, (int, float)): raise TypeError
#     if len(set(spisok)) != 2: raise ValueError
#
#     dct = {}
#     for i in spisok:
#         dct[i] = dct.get(i, 0) + 1
#     lst = sorted(dct, key=lambda x: (-dct[x], x))
#     for i in lst:
#         if dct[i] == 1:
#             return i
# # 3 2 2 2 2
#
# class TestCubeAtea(unittest.TestCase):
#     def test_one(self):
#         self.assertEqual(one([1, 1, 1, 2]), 2)
#         self.assertEqual(one([1, 1, 2, 1]), 2)
#         self.assertEqual(one([2, 1, 1, 1]), 2)
#     def test_value(self):
#         self.assertRaises(ValueError, one, [])
#         self.assertRaises(ValueError, one, [123])
#         self.assertRaises(ValueError, one, [123, 234])
#         self.assertRaises(ValueError, one, [123, 123])
#         self.assertRaises(ValueError, one, [1, 1, 1, 1, 1])
#         self.assertRaises(ValueError, one, [1, 2, 3, 3, 3])
#     def test_type(self):
#         self.assertRaises(TypeError, one, tuple())
#         self.assertRaises(TypeError, one, ['123', 1, 1])
#
# if __name__ == '__main__':
#     print(one([3, 2, 2, 2, 2]))
#     # print(one([2, 2, 3, 2, 2]))
#     unittest.main()

