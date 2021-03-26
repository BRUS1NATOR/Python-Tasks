def custom_pow(num, power):
    temp = num
    while power > 1:
        num *= temp
        power -= 1
    return num


def user_input():
    try:
        number = float(input('Введите число: '))
    except ValueError or TypeError:
        print('Ошибка при вводе числа')
        user_input()
    try:
        power = int(input('Введите степень: '))
        print(custom_pow(number, power))
    except ValueError or TypeError:
        print('Степень должна быть целым числом и больше нуля')
        user_input()


if __name__ == '__main__':
    user_input()
