import re


def user_input():
    try:
        s = input('Введите выражение: ')

        numbers = re.split(r'\+|-|\*|\/|\s', s)
        numbers = list(filter(None, numbers))

        if len(numbers) != 2:
            print('Количество чисел должно быть равно 2')
            raise ValueError
        else:
            numbers = list(map(float, numbers))

        signs = re.findall(r'\+|-|\*|/', s)
        signs = list(filter(None, signs))

        if len(signs) == 1:
            exec('print(' + str(numbers[0]) + str(signs[0]) + str(numbers[1]) + ')')
        elif len(signs) == 0:
            print('Не найден подходящий знак операции (+,-,*,/)')
            raise ValueError
        else:
            print('Знаков операции должно быть не более 1')
            raise ValueError

    except ValueError:
        user_input()


if __name__ == '__main__':
    user_input()