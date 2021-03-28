from enum import Enum

K_MAX = 12
k_now = 0
frequency_drawn_numbers = {0: 0}  # key = номер, value = количество выпавших раз
drawn_numbers = []


def get_possible_numbers():
    result = []
    for i in range(0, 36):
        result.append(i)
    return result


def get_most_frequent_number(number_drawn):
    global frequency_drawn_numbers

    if number_drawn in frequency_drawn_numbers:
        frequency_drawn_numbers[number_drawn] += 1
    else:
        frequency_drawn_numbers[number_drawn] = 1

    max_freq = frequency_drawn_numbers[
        max(frequency_drawn_numbers, key=lambda y: frequency_drawn_numbers[y])]  # Почему то возвращает ключ idk

    result = []
    for x in frequency_drawn_numbers:
        if frequency_drawn_numbers[x] == max_freq:
            result.append(x)
    return result


def get_not_drawn(number_drawn):
    global k_now
    global drawn_numbers

    drawn_numbers.append(number_drawn)
    k_now += 1
    if K_MAX < k_now:
        return list(set(get_possible_numbers()) ^ set(drawn_numbers[k_now-K_MAX:len(drawn_numbers)]))
    else:
        return list(set(get_possible_numbers()) ^ set(drawn_numbers))


def get_color_history():
    result = []
    colors = list(map(get_color, drawn_numbers))
    result.append(colors.count(Color.RED))
    result.append(colors.count(Color.BLACK))
    return result


class Color(Enum):
    GREEN = 0
    RED = 1
    BLACK = 2


def get_color(num):
    if num == 0:
        return Color.GREEN
    if num % 2 == 0:
        return Color.BLACK
    return Color.RED


def user_input():
    try:
        x = int(input('Введите целое число -36 <= x <= 36: '))
        if not -36 <= x <= 36:
            raise ValueError
        if x < 0:
            return

        print(*get_most_frequent_number(x), sep=' ')
        print(*get_not_drawn(x), sep=' ')
        print(*get_color_history(), sep=' ')

        user_input()

    except ValueError or TypeError:
        print('Число должно быть целым и в промежутке -36 <= x <= 36')
        user_input()


if __name__ == '__main__':
    user_input()
