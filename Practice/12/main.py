def factorial(num):
    result = num
    while num > 1:
        num -= 1
        result *= num
    return result


def user_input():
    try:
        number = int(input('Введите число: '))
        if number < 0:
            raise ValueError
        print(factorial(number))
    except ValueError or TypeError:
        print('Ошибка при вводе целого, положительного числа')
        user_input()


if __name__ == '__main__':
    user_input()
