from matplotlib import pyplot as plt, patches

from lab_python_oop import Figure
from lab_python_oop.color import FigureColor
from math import pi


class Circle(Figure):
    __type__ = "Круг"

    @classmethod
    def get_type(cls):
        return cls.__type__

    def __init__(self, _radius, _color):
        self.radius = _radius
        self.color = FigureColor()
        self.color.colorproperty = _color

    def square(self):
        return self.radius ** 2 * pi

    def __repr__(self):
        return '{} цвета {} радиусом {} площадью {}.'.format(
            Circle.get_type(),
            self.color.colorproperty,
            self.radius,
            self.square()
        )

    def draw(self):
        fig, ax = plt.subplots()
        ax.plot([1, 1, 1], [1, 1, 1], color="cyan")
        ax.add_patch(patches.Circle((0, 0), self.radius, color=self.color.colorproperty))
        plt.xlabel("X-AXIS")
        plt.ylabel("Y-AXIS")
        plt.title("PLOT-1")
        plt.show()
