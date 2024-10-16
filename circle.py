import math


def area(r):
    '''
    Принимает радиус и возвращает площадь круга

    Пример вызова:
        circle_area = area(10)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус и возвращает периметр окружности

    Пример вызова:
        circle_perimeter = perimeter(10)
    '''
    return 2 * math.pi * r

