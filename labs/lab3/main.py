from time import sleep

from lab_python_fp.field import *
from lab_python_fp.gen_random import *
from lab_python_fp.unique import *
from lab_python_fp.print_result import *
from lab_python_fp.cm_timer import *


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
    for i in Unique(data, ignore_case=True):
        print(i)


def main5():
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()


def main6():
    with cm_timer_1():
        sleep(5.5)
    with cm_timer_2():
        sleep(5.5)


if __name__ == "__main__":
    main6()
