def check_if_prime(n):
    temp = 2
    while n % temp != 0:
        temp += 1
    if temp == n:
        return 'Простое'
    else:
        return 'Составное'


def user_input():
    try:
        number = int(input('Введите целое число в промежутке 2 <= x <= 10**9: '))
        if 2 <= number <= 10**9:
            print(check_if_prime(number))
        else:
            raise ValueError

    except ValueError or TypeError:
        print('Число должно быть целым и в промежутке 2 <= x <= 10**9')
        user_input()


if __name__ == '__main__':
    user_input()
