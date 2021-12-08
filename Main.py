import math


def func(x):
    return math.sin(x)+0.3-1.4*x*x


def func_first(x):
    return math.cos(x) - 2.8*x


def func_second(x):
    return -math.sin(x) - 2.8


def fi(x):
    return math.sqrt((math.sin(x) + 0.3) / 1.4)


def epsilon():
    return 0.000005


def checking_the_segment(segment):
    result = func(segment[0]) * func(segment[1])
    if result >= 0:
        raise Exception("Неверный отрезок")
    print("Корень лежит на отрзке [" + str(segment[0]) + ", " + str(segment[1]) + "]")
    print("Произведение функции от концов отрезка = " + str(result) + " (меньше 0)")


def checking_starting_point(x0):
    result = func(x0) * func_second(x0)
    if result <= 0:
        raise Exception("Неверная начальная точка")
    print("Начальная точка: " + str(x0))
    print("func(x0) * func_second(x0) = " + str(result) + " (больше 0)")


def method_of_half_division(segment):
    left, right = segment
    eps = epsilon()
    count = 0
    number_of_steps = math.ceil(math.log((segment[1] - segment[0])/eps, 2))
    while math.fabs(func((left+right)/2)) >= eps and number_of_steps >= count:
        count += 1
        middle = (left + right)/2
        if func(left)*func(middle) < 0:
            right = middle
        elif func(middle)*func(right) < 0:
            left = middle
        else:
            raise Exception("Неверный отрезок")
    if math.fabs(func((left+right)/2)) >= eps:
        raise Exception("Неверная точность.")
    result = (right + left)/2
    print("Метод половинного деления: ")
    print(" Число шагов: " + str(count))
    print(" Корень: " + str(result))


def Newtons_method(x0):
    eps = epsilon()
    xn = x0
    count = 0
    while True:
        count += 1
        new = xn - func(xn)/func_first(xn)
        if math.fabs(new - xn) < eps:
            print("Метод Ньютона: ")
            print(" Число шагов: " + str(count))
            print(" Корень: " + str(new))
            break
        xn = new


def modified_Newtons_method(x0):
    eps = epsilon()
    xn = x0
    count = 0
    while True:
        count += 1
        new = xn - func(xn)/func_first(x0)
        if math.fabs(new - xn) < eps:
            print("Модифицированный метод Ньютона: ")
            print(" Число шагов: " + str(count))
            print(" Корень: " + str(new))
            break
        xn = new


def chord_method(segment, x0):
    eps = epsilon()
    if x0 == segment[0]:
        xn = segment[1]
    elif x0 == segment[1]:
        xn = segment[0]
    else:
        raise Exception("Неверный x0")
    count = 0
    while True:
        count += 1
        new = xn - func(xn)*(xn-x0)/(func(xn) - func(x0))
        if math.fabs(new - xn) < eps:
            print("Метод хорд: ")
            print(" Число шагов: " + str(count))
            print(" Корень: " + str(new))
            break
        xn = new


def method_of_movable_chords(segment, x0):
    prev = x0
    eps = epsilon()
    if x0 == segment[0]:
        xn = segment[1]
    elif x0 == segment[1]:
        xn = segment[0]
    else:
        raise Exception("Неверный x0")
    count = 0
    while True:
        count += 1
        new = xn - func(xn)*(xn-prev)/(func(xn) - func(prev))
        if math.fabs(new - xn) < eps:
            print("Метод подвижных хорд: ")
            print(" Число шагов: " + str(count))
            print(" Корень: " + str(new))
            break
        prev = xn
        xn = new


def simple_iteration_method(x0):
    eps = epsilon()
    xn = x0
    count = 0
    while True:
        count += 1
        new = fi(xn)
        if math.fabs(new - xn) < eps:
            print("Метод простой итерации: ")
            print(" Число шагов: " + str(count))
            print(" Корень: " + str(new))
            break
        xn = new


def main():
    segment = (0.5, 1.5)
    x0 = 1.5
    checking_the_segment(segment)
    checking_starting_point(x0)
    method_of_half_division(segment)
    Newtons_method(x0)
    modified_Newtons_method(x0)
    chord_method(segment, x0)
    method_of_movable_chords(segment, x0)
    simple_iteration_method(x0)


if __name__ == '__main__':
    main()
