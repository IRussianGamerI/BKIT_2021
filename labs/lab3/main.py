from lab_python_fp.field import *


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print(field(goods, 'title'))


if __name__ == "__main__":
    main()
