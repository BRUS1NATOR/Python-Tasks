def find_pare(r1, r2, index1, index2, target):
    if r1[index1] + r2[index2] == target:
        return [r1[index1], r2[index2]]
    else:
        index2 += 1
        if index2 < len(r2):
            return find_pare(r1, r2, index1, index2, target)
        else:
            index1 += 1
            if index1 < len(r1):
                return find_pare(r1, r2, index1, index2, target)
            else:
                return -1


def user_input():
    try:
        numbers = list(map(int, input('Введите числа: ').split()))

        if len(numbers) != 5:
            print('Необходимо 5 чисел')
            raise ValueError

        r1 = numbers[1:3]
        r2 = numbers[3:5]

        if r1[0] + r2[0] <= numbers[0] <= r1[1] + r2[1]:
            print(*find_pare(r1, r2, 0, 0, numbers[0]))
        else:
            print(-1)

    except ValueError or TypeError:
        user_input()


if __name__ == '__main__':
    user_input()
