from abstract import ABMI


class my_BMI(ABMI):
    # Принимает вес в килограммах и рост в метрах. Возвращает индекс массы тела.
    def bmi(self, weight: float, height: float):
        super().bmi(weight, height)
        return weight / ((height / 100) ** 2)

    # Принимает численное значение ИМТ и печатает на экран соответствующую категорию
    def print_bmi(self, _bmi: float):
        super().print_bmi(_bmi)
        if _bmi < 18.5:
            print('Underweight')
        elif 18.5 <= _bmi < 25.0:
            print('Normal')
        elif 25 <= _bmi < 30.0:
            print('Overweight')
        else:
            print('Obesity')


def user_input():
    try:
        data = list(map(float, input('Введите вес и рост через пробел: ').split(' ')))
        if len(data) == 2:
            my_BMI().print_bmi(my_BMI().bmi(data[0], data[1]))

    except ValueError or TypeError:
        print('Введите вес и рост должны быть числами')
        user_input()


if __name__ == '__main__':
    user_input()
