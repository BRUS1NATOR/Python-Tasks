import os
import sys


def tryExecFile(path, file_name):
    print('Пытаюсь открыть:', path)
    try:
        sys.path.append(path)   # Для 21 лабы (import)
        exec(open(path + file_name, encoding='utf-8').read(), globals())
        user_proceed()
    except FileNotFoundError:
        print('Файл не найден')
        user_input()


def user_input():
    num = int(input('Введите номер практического задания: '))
    if num < 10:
        num = '0' + str(num)
    path = os.path.dirname(os.path.realpath(__file__)) + "\\Practice\\" + str(num)
    tryExecFile(path, "\\main.py")


def user_proceed():
    yesOrNo = input('Открыть другое задание(y/n)?: ')
    if yesOrNo.__contains__('y') or yesOrNo.__contains__('д'):
        user_input()
    else:
        return


if __name__ == '__main__':
    user_input()