class Shape:
    def __init__(self):
        self.Name = input('Введите название объекта: ')
        self.Colour = input('Введите цвет: ')
        self.Square = input('Введите площадь: ')
    def info(self):
        print(f'{self.Name}, {self.Colour}, {self.Square}')

    # @staticmethod
    def Col(self, txt):
        if txt == self.Colour:
            print(f'{self.Name}, {self.Colour}, {self.Square}')
        else:
            print('У данной фигуры другой цвет')

    def Sq(self):
        print(f'{self.Name}, {self.Square}')


Shape_1 = Shape()
Shape_2 = Shape()
Shape_3 = Shape()

Shape_1.Col('Красный')
Shape_2.Col('Синий')
Shape_3.Col('Зеленый')

Shape_1.Sq()
Shape_2.Sq()
Shape_3.Sq()

