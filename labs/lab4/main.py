from sys import argv
from math import sqrt


def get_coef(index, msg):
    try:
        coef = float(argv[index])
    except:
        switch = True
        while switch:
            try:
                coef = float(input(msg))
                switch = False
            except:
                switch = True
    return coef


def discriminant(a, b, c):
    return b**2 - 4*a*c


def solve_square(a, b, c):
    roots = set()
    d = discriminant(a, b, c)
    if d >= 0:
        roots.add((-b-sqrt(d))/(2*a))
        roots.add((-b+sqrt(d))/(2*a))
    return roots


def solve_bisquare(a, b, c):
    roots = set()
    square_roots = solve_square(a, b, c)
    for root in square_roots:
        if root >= 0:
            roots.add(sqrt(root))
            roots.add(-sqrt(root))
    return roots


def main():
    a = get_coef(1, "Введите a:")
    b = get_coef(2, "Введите b:")
    c = get_coef(3, "Введите c:")
    if a == b == c == 0:
        print("Количество корней: ∞", "x ∈ ℝ", sep='\n')
        return
    roots = solve_bisquare(a, b, c)
    print("Количество корней:", len(roots))
    for root in roots:
        print(root, end=" ")


if __name__ == '__main__':
    main()
