def area(a, b):
    '''
    Принимает на вход длину и ширину прямоугольника и возвращает его площадь.

        Параметры:
            a (int): длина
            b (int): ширина

        Возвращаемое значение:
            area (int): площадь прямоугольника
        
        Пример вызова:
            rectangle_area = area(10, 12)
    '''

    a_value = int(a);
    b_value = int(b);

    if (a_value <= 0 or b_value <= 0):
        raise ValueError("Values must be positive integers")

    return a_value * b_value


def perimeter(a, b):
    '''
    Принимает на вход длину и ширину прямоугольника и возвращает его периметр.

        Параметры:
            a (int): длина
            b (int): ширина

        Возвращаемое значение:
            perimeter (int): периметр прямоугольника

        Пример вызова:
            rectangle_perimeter = perimeter(10, 12)
    '''

    a_value = int(a);
    b_value = int(b);

    if (a_value <= 0 or b_value <= 0):
        raise ValueError("Values must be positive integers")

    return (a_value + b_value) * 2

