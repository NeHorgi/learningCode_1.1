'''

Реализовать 2D-движок, который умеет “рисовать” простейшие
двумерные примитивы на экране. Сам движок должен быть
представлен в виде объекта класса Engine2D.

• Движок должен иметь “холст” (canvas) и возможность добавлять
на него фигуры. Холст будет содержать текущий список
примитивов для отрисовки.

• Реализовать классы для 3-х геометрических фигур: окружность,
треугольник, прямоугольник. Необходимые параметры для
создания фигур выбрать самостоятельно.

• Каждая фигура должна иметь метод draw(), при вызове которого
выводится информация в виде print’а, например “Drawing Circle:
(0, 1) with radius 5”.

• При завершении добавления фигур, у движка необходимо
вызвать публичный метод draw(), который последовательно
вызовет методы для отрисовки у всех фигур на холсте и очистит
его.

• Добавить возможность менять цвет отрисовки, путем вызова
публичного метода у движка (можно воспринимать это как
«смена карандаша»):

        • После вызова этого метода, все последующие фигуры
    должны рисоваться указанным цветом, до очередного
    выставления нового цвета.

        • В тексте “отрисовки” фигуры должен появиться цвет,
    которым она будет рисоваться.

        • Написать юниттесты с использованием pytest. Необходимое
    количество тестов определить самостоятельно

'''


class Figure:

    def __init__(self, name):
        self.name = name

    def parameters(self):
        return None

    def draw(self):
        return print(f'Drawing {self.name}: {self.parameters()}{self.color if self.color else "."}')


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__('Triangle')

    def parameters(self):
        return f'with {self.a}, {self.b} and {self.c} sides'


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__('Rectangle')

    def parameters(self):
        return f'with {self.a} and {self.b} sides'


class Circle(Figure):

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        super().__init__('Circle')

    def parameters(self):
        return f'with center in {self.center} and {self.radius} radius'


class Engine2D:

    def __init__(self):
        self.color = None
        self.canvas = []

    def add(self, obj):
        obj.color = self.color
        self.canvas.append(obj)

    def draw(self):
        for obj in self.canvas:
            obj.draw()
        self.canvas = []

    def set_color(self, color):
        self.color = f', {color} color'


if __name__ == '__main__':
    triangle = Triangle(10, 10, 10)
    rectangle = Rectangle(10, 10)
    circle = Circle((0.0), 5)

    engine = Engine2D()

    engine.add(circle)
    engine.add(rectangle)

    engine.set_color('blue')

    engine.add(triangle)

    circle_1 = Circle((1.1), 7)
    engine.add(circle_1)

    engine.set_color('green')

    rectangle_1 = Rectangle(7, 7)
    engine.add(rectangle_1)

    engine.draw()
