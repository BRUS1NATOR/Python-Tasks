import re


class TicketCountError(Exception):
    pass


def user_input():
    try:
        number = int(input('Введите количество билетов Сигизмунда в промежутке 1 <= x <= 10^9: '))
        if 1 <= number <= 10 ** 9:
            tickets = input('Введите билеты через пробел: ').split(' ')

            if len(tickets) != number:
                raise TicketCountError

            regex = r"(^a[a-z0-9]{3}55661)"
            r = re.compile(regex)

            result = list(filter(r.match, tickets))

            if len(result) == 0:
                print(-1)
            else:
                print(*result, sep=' ')

        else:
            raise ValueError

    except ValueError or TypeError:
        print('Количество билетов должно быть целым и в промежутке 1 <= x <= 10^9')
        user_input()
    except TicketCountError:
        print('Количество билетов не соответсвует введенным билетам')
        user_input()


if __name__ == '__main__':
    user_input()