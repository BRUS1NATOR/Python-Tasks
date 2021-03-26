def date_input():
    s = input('Введите дату: ')
    numbers = s.split(':')
    numbers = list(filter(None, numbers))

    if len(numbers) != 2:
        print(numbers)
        print('Количество чисел должно быть равно 2')
        raise ValueError
    else:
        numbers = list(map(int, numbers))

    if not 0 < numbers[0] < 24:
        print('Часы не корректны')
        raise ValueError
    if not 0 < numbers[1] < 60:
        print('Минуты не корректны')
        raise ValueError

    return numbers


def user_input():
    try:
        s = date_input()
        time1 = s[0] * 60 + s[1]

        s = date_input()
        time2 = s[0] * 60 + s[1]

        result = (('Встреча состоится', 'Встреча не состоится')[time1 > time2 + 15],
                  ('Встреча состоится', 'Встреча не состоится')[time2 > time1 + 15])[time1 < time2]
        print(result)

    except ValueError or TypeError:
        user_input()


if __name__ == '__main__':
    user_input()
