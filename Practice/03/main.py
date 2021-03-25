if __name__ == '__main__':
    a, b = map(int, input("Введите два числа: ").split())
    # + - * /
    print("{aInt}+{bInt}=".format(aInt=a, bInt=b), a + b, sep='')
    print("{aInt}-{bInt}=".format(aInt=a, bInt=b), a - b, sep='')
    print("{aInt}*{bInt}=".format(aInt=a, bInt=b), a * b, sep='')
    print("{aInt}/{bInt}=".format(aInt=a, bInt=b), a / b, sep='')