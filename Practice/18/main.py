import re

known_words = ['hallo', 'klempner', 'das', 'ist', 'fantastisch', 'fluggegecheimen']
letter_possibility = {}


def init_dictionary():
    global letter_possibility

    letters_total = 0
    for word in known_words:
        letters_total += len(word)
        for letter in word:
            if letter in letter_possibility:
                letter_possibility[letter] += 1
            else:
                letter_possibility[letter] = 1

    for letter in letter_possibility:
        letter_possibility[letter] /= letters_total
    # print(letter_possibility)


def calculate(stop_word):
    probability = letter_possibility[stop_word[0]]
    for letter in range(1, len(stop_word)):
        probability *= letter_possibility[stop_word[letter]]
    return probability


def user_input():
    try:
        stop_word = input('Введите стоп-слово: ')

        if re.match(r'([a-zA-Z]+$)', stop_word):
            init_dictionary()
            print(calculate(stop_word))

        else:
            raise ValueError

    except ValueError or TypeError:
        print('Слово не должно содержать символы или цифры')
        user_input()


if __name__ == '__main__':
    user_input()
