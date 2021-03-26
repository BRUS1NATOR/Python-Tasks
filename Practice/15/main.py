import random
MAX_ATTEMPT = 5
rand_number = 0


def start_game():
    print('Угадайте число 0 <= x <= 100')
    global rand_number
    rand_number = random.randint(0, 100)
    user_input(0)


def guess(n):
    if rand_number == n:
        return 'win'
    elif rand_number < n:
        return 'smaller'
    else:
        return 'bigger'


def user_input(attempt):
    if attempt >= MAX_ATTEMPT:
        inp = input('Хотите начать сначала? (1 - ДА )')
        if inp == '1':
            start_game()
        else:
            quit()
    else:
        try:
            number = int(input())
            msg = guess(number)
            if msg == 'win':
                print('Поздравляю! Вы угадали')
                user_input(MAX_ATTEMPT)
            elif msg == 'smaller':
                print('Загаданное число меньше')
            else:
                print('Загаданное число больше')
            attempt += 1
            if attempt >= MAX_ATTEMPT:
                print(f'Вы проиграли. Было загадано: {rand_number}')
            user_input(attempt)

        except ValueError or TypeError:
            print('Число должно быть целым и в промежутке 0 <= x <= 100')
            user_input(attempt)


if __name__ == '__main__':
    start_game()
