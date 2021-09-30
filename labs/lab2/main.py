from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle(3, 2, "blue")
    c = Circle(5, "green")
    s = Square(5, "red")
    print(r)
    r.draw()
    print(c)
    print(s)


if __name__ == "__main__":
    main()
