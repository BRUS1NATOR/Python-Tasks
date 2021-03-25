import math


def xy_input(message):
    val = list(map(float, (input(message).split())))

    if len(val) == 2:
        return val
    raise ValueError


def user_input():
    try:
        method = int(input('Выберите тип ввода(1 - стороны, 2 - вершины) '))

        if math.fabs(method > 1000):
            raise ValueError

        if method == 1:
            a = float(input('Введите a: '))
            b = float(input('Введите b: '))
            c = float(input('Введите c: '))
            print('S =', calculate_bysides(a, b, c))
        else:
            a = xy_input('Введите A: ')
            b = xy_input('Введите B: ')
            c = xy_input('Введите C: ')
            print('S =', calculate_bydots(a, b, c))

    except ValueError:
        user_input()


def calculate_bydots(a, b, c):
    mx1 = a[0] - c[0]
    mx2 = b[0] - c[0]
    my1 = a[1] - c[1]
    my2 = b[1] - c[1]
    return math.fabs(mx1*my2-mx2*my1)/2


def calculate_bysides(a, b, c):
    if a+b < c or a+c < b or c+b < a:
        return 'Треугольника с заданными сторонами не существует'
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


if __name__ == '__main__':
    user_input()
