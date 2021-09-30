from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
from matplotlib import patches

class Rectangle(Figure):
    __type__ = "Прямоугольник"

    @classmethod
    def get_type(cls):
        return cls.__type__

    def __init__(self, _width, _height, _color):
        self.width = _width
        self.height = _height
        self.color = FigureColor()
        self.color.colorproperty = _color

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_type(),
            self.color.colorproperty,
            self.width,
            self.height,
            self.square()
        )

    def draw(self):
        patches.Rectangle((0, 0), self.width, self.height, color=self.color.colorproperty)
