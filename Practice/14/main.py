def check_num(n):
    temp = 0
    while 2**temp <= n:
        temp += 1
    return temp


def user_input():
    try:
        number = int(input('Введите целое число в промежутке 0 <= x <= 10**15: '))
        if 0 <= number <= 10**15:
            print(check_num(number))
        else:
            raise ValueError

    except ValueError or TypeError:
        print('Число должно быть целым и в промежутке 0 <= x <= 10**15')
        user_input()


if __name__ == '__main__':
    user_input()
