def print_values(a, b):
    print(a)
    print(b)


if __name__ == '__main__':
    coolNum = 8001
    coolerNum = 42

    # Поменять местами
    temp = coolNum
    coolNum = coolerNum
    coolerNum = temp
    print_values(coolNum, coolerNum)

    # Поменять местами без 3 переменной
    coolNum, coolerNum = coolerNum, coolNum
    print_values(coolNum, coolerNum)