def check_if_prime(n):
    temp = 2
    while n % temp != 0:
        temp += 1
    if temp == n:
        return n
    else:
        return 0


def decompose_number(number, result):
    for prime in prime_nums:
        if number % prime == 0:
            number = number / prime
            if prime in result:
                result[prime] += 1
            else:
                result[prime] = 1
            return decompose_number(number, result)
    if number > 1:
        result[number] = 1


prime_nums = []


def user_input():
    global prime_nums
    try:
        number = int(input("Введите целое число x (1<=x<=10^9): "))

        if not 1 <= number <= 10 ** 9:
            raise ValueError

        # Считаем простые числа зараннее
        for i in range(2, number):
            temp = check_if_prime(i)
            if temp != 0:
                prime_nums.append(temp)

        result = {}
        decompose_number(number, result)

        s = ""
        for i in result:
            if result[i] > 1:
                s += '*' + str(i) + '^' + str(result[i])
            else:
                s += '*' + str(i)
        s = s[1:len(s)]

        print(s)

    except ValueError or TypeError:
        print('Число должно быть целым и в промежутке 2 <= x <= 10**9')
        user_input()


if __name__ == '__main__':
    user_input()
