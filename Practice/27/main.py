import random
from math import sqrt


def BozoSort(values, asc=True):
    # если 2д массив
    if isinstance(values[0], list):
        temp = []
        for i in values:
            for j in i:
                temp.append(j)
        values = temp
    #

    index1 = random.randint(0, len(values)-1)
    index2 = random.randint(0, len(values)-1)
    while index1 == index2:
        index2 = random.randint(0, len(values)-1)

    values[index1], values[index2] = values[index2], values[index1]

    for i in range(0, len(values)):
        if i >= len(values) - 1:
            return values
        elif asc:
            if values[i] > values[i+1]:
                return BozoSort(values, asc)
        else:
            if values[i] < values[i+1]:
                return BozoSort(values, asc)


def user_input():
    try:
        n = int(input('Введите количество чисел n (1<=n<=100000): '))

        if 1 <= n <= 100000:
            numbers = list(map(int, input(f'Введите несколько ({n}) чисел: ').split(' ')))
            if len(numbers) != n:
                print('Неверное количество чисел')
                raise ValueError

            start_offset = 0
            for i in range(0, n):
                print(*sorted(numbers[0:i+1])[0:5].__reversed__(), sep=' ')

        else:
            print('Неверное количество чисел')
            raise ValueError

    except ValueError or TypeError:
        user_input()


if __name__ == '__main__':
    user_input()
