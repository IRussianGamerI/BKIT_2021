from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    def __init__(self, _width, _height, _color):
        self.width = _width
        self.height = _height
        self.color = FigureColor()
        self.color.colorproperty = _color

    def square(self):
        return self.width * self.height


