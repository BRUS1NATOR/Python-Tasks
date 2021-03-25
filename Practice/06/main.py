import math

G = 9.8


def calculate_roots(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


if __name__ == '__main__':
    a, b, c = map(float, input("Введите a, b, c: ").split())
    print(calculate_roots(a, b, c))
