import os
import sys


def tryExecFile(path):
    print('Пытаюсь открыть:', path)
    try:
        fsenc = sys.getfilesystemencoding()
        exec(open(path, encoding='utf-8').read())
        userProceed()
    except FileNotFoundError:
        print('Файл не найден')
        userInput()


def userInput():
    num = int(input('Введите номер практического задания: '))
    if num < 10:
        num = '0' + str(num)
    path = os.path.dirname(os.path.realpath(__file__)) + "\\Practice\\" + str(num) + "\\main.py"
    tryExecFile(path)


def userProceed():
    yesOrNo = input('Открыть другое задание(y/n)?: ')
    if(yesOrNo.__contains__('y') or yesOrNo.__contains__('д')):
        userInput()
    else:
        return

if __name__ == '__main__':
    userInput()