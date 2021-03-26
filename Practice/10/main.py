def create_dic(x1, x2):
    return {'x1': x1, 'x2': x2, 'sumIsNull': x1+x2 == 0}


def user_input():
    try:
        numbers = list(map(int, input('Введите числа: ').split()))

        if len(numbers) != 5:
            print('Необходимо 5 чисел')
            raise ValueError

        r1 = numbers[1:3]
        r2 = numbers[3:5]

        c1 = list(map(lambda x, y: create_dic(x, y), r1, r2))
        c2 = list(map(lambda x, y: create_dic(x, y), r1, reversed(r2)))

        result = list(filter(lambda x: x['sumIsNull'] == True, c1 + c2))

        if len(result) > 0:
            result = sorted(result, key=lambda x: x['x1'])
            print(result[0]['x1'], result[0]['x2'])
        else:
            print(-1)

    except ValueError or TypeError:
        user_input()


if __name__ == '__main__':
    user_input()
