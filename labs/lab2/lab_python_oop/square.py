from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):

    __type__ = "Квадрат"

    @classmethod
    def get_type(cls):
        return cls.__type__

    def __init__(self, _side, _color):
        self.side = _side
        super().__init__(self.side, self.side, _color)

    def __repr__(self):
        return '{} цвета {} со стороной {} площадью {}.'.format(
            Square.get_type(),
            self.color.colorproperty,
            self.side,
            self.square()
        )
