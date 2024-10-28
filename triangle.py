def area(a, h):
    '''
    Принимает высоту и основание треугольника и вычисляет его площадь по формуле

    Пример вызова:
        triangle_area = area(5, 12)
    '''
    return int(a) * int(h) / 2 


def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника по трём его сторонам
        Параметры:
            a (int) сторона
            b (int) сторона
            c (int) сторона

        Возвращаемое значение:
            perimeter (int) периметр треугольника

        Пример вызова:
            triangle_perimeter = perimeter(5, 12)
    '''
    return int(a) + int(b) + int(c)

