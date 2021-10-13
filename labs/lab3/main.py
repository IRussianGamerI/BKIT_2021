from lab_python_fp.field import *
from lab_python_fp.gen_random import *
from lab_python_fp.unique import *


def main1():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    gen_res = field(goods, 'title', 'price')
    for item in gen_res:
        print(item)


def main2():
    res = gen_random(5, 1, 5)
    for item in res:
        print(item)


def main3():
    data = ["A", "B", "a", "b"]
    while True:
        for i in Unique(gen_random(5, 1, 2)):
            print(i)


if __name__ == "__main__":
    main3()
