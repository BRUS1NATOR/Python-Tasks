G = 9.8

def calculate_distance(x0, v0, t):
    return x0 * v0 * t - G * t ** 2

if __name__ == '__main__':
    x0, v0, t = map(float, input("Введите x0,v0,t: ").split())
    print(calculate_distance(x0, v0, t))