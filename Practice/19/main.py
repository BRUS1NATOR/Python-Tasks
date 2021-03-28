import re

known_words = ['hallo', 'klempner', 'das', 'ist', 'fantastisch', 'fluggegecheimen']
letter_possibility = {}


def calculate(letters, length):
    set(letters)
    return add_letter("", letters, 0, length)


def add_letter(target, letters, step, n):
    step += 1
    result = []
    for i in letters:
        s = target
        s += i

        allowed_duplicates = 1
        if len(letters) < n:
            allowed_duplicates = n - len(letters) + 1

        if s.count(i) <= allowed_duplicates:
            if step < n:
                result += add_letter(s, letters, step, n)
            else:
                result.append(s)

    return result


def user_input():
    try:
        code_len = int(input('Введите длину пароля (0<=x<=8): '))
        if not 1 <= code_len <= 8:
            print('Длина пароля должна быть не меньше 1 и не больше 8')
            raise ValueError

        code_word = input('Введите возможные символы входящие в пароль (a-z): ')

        if re.match(r'([a-zA-Z]+$)', code_word):
            print(*calculate(code_word, code_len), sep=' ')

        else:
            print('Слово не должно содержать символы и цифры')
            raise ValueError

    except ValueError:
        user_input()
    except TypeError:
        print('Длина пароля должна быть числом')
        user_input()


if __name__ == '__main__':
    user_input()