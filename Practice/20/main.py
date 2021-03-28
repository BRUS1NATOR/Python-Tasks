import re

all_drinks = []


class Drink:
    Name = ''
    Price = 0
    Volume = 0

    def __init__(self, s):
        s = s.split(' ')
        if len(s) != 3:
            raise ValueError
        self.Name = s[0]
        self.Price = int(s[1])
        self.Volume = int(s[2])

        if not 1 <= self.Price <= 10**9 \
                or not 1 <= self.Volume <= 10**9 \
                or not re.match('([a-zA-Z]+$)', self.Name):
            raise ValueError


def drinks_input(drinks_count):
    for i in range(0, drinks_count):
        create_drink()


def create_drink():
    global all_drinks
    try:
        bottle = input('Введите имя напитка, цену напитка и его объем через пробел: ')
        all_drinks.append(Drink(bottle))
    except ValueError or TypeError:
        print('Ошибка, попробуйте повторить')
        create_drink()


def calculate(money):
    global all_drinks
    result = []
    temp = []
    for drink in all_drinks:
        result += stupid_function(temp, all_drinks, drink, money, 0)
    return result


def stupid_function(result, drinks, drink_now, money, volume):

    result.append(drink_now)
    money -= drink_now.Price
    volume += drink_now.Volume

    for drink in drinks:
        if money >= drink.Price:
            stupid_function(result, drinks, drink, money, volume)
        else:
            return result


def user_input():
    # try:
    money = int(input('Введите количество денег (0<=x<=10^9): '))
    if not 0 <= money <= 10 ** 9:
        print('Количество денег должно быть не меньше 0 и не больше 10^9')
        raise ValueError

    drink_types = int(input('Введите количество разновидностей напитков (1<=x<=10^9): '))
    if not 1 <= drink_types <= 10 ** 9:
        print('Количество напитков должно быть не меньше 1 и не больше 10^9')
        raise ValueError

    drinks_input(drink_types)
    for i in calculate(money):
        print(i.Name)
        # for v in i:
        #     print(v)



# except ValueError:
#     print('err')
#     user_input()
# except TypeError:
#     print('err')
#     user_input()

if __name__ == '__main__':
    user_input()
