import re


class TicketCountError(Exception):
    pass


def user_input():
    try:
        number = int(input('Введите количество билетов Сигизмунда в промежутке 1 <= x <= 10^9: '))
        if 1 <= number <= 10 ** 9:
            tickets = input('Введите билеты через пробел: ')

            if len(tickets.split(' ')) != number:
                raise TicketCountError

            regex = r"(^[a-z]{2}[0-9]{2}55661)"
            result = re.findall(regex, tickets)

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