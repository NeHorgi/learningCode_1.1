import pytest


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
        super().__init__(self.__class__.__name__)

    def parameters(self):
        return f'with {self.a}, {self.b} and {self.c} sides'
    # TODO __repr__ or __str__ посмотреть!!!
    # TODO снова нейминг!!!


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

    def draw(self):
        raise RuntimeError('')


class Engine2D:

    def __init__(self):
        self.color = None
        self.canvas = []

    def add(self, obj): #11
        obj.color = self.color
        self.canvas.append(obj)

    def draw(self):
        for obj in self.canvas:
            obj.draw()
        self.canvas = []
    # TODO найти тут багло(представим, что при отрисовке вылезает ошибка)
    # В ходе отрисовки любого обьекта возникает ошибка, в ходе чего в функции draw появляется багло, найти причину и решение

    def set_color(self, color):
        self.color = f', {color} color.'


class TestUnit:

    def test_empty_canvas(self):

        engine_test = Engine2D() # Можно сделать фикстурой, так как постоянно используем

        engine_test.add(Triangle(10, 10, 10))
        assert engine_test.canvas

        # TODO добавить ту же проверку состояния, как пример
        # расширить спектр сценариев для тестирования
        # проверять не только то, что что-то появилось, но и то, что появилось
        # проверка на тот же типа данных на ввод, например
        # TODO анотации!!!!!

    def test_changed_color(self):

        engine_test = Engine2D()

        engine_test.set_color('white')
        assert engine_test.color


    def test_draw_figure(self):

        engine_test = Engine2D()

        engine_test.add(Triangle(10, 10, 10))
        drawing = engine_test.draw()

        assert str(drawing)

    def test_figure_name(self):

        triangle = Triangle(10, 10, 10)

        assert triangle.name == 'Triangle'

    def test_figure_parametrs(self):

        triangle = Triangle(10, 10, 10)
        parametrs = triangle.parameters()

        assert str(parametrs)

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