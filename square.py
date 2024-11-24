
def area(a):
    '''
    Возвращает площадь квадрата

    Пример вызова:
        square_area = area(6)
    '''

    a_value = int(a);

    if (a_value <= 0):
        raise ValueError("Value must be positive integers")
    
    return a_value * a_value


def perimeter(a):
    '''
    Возвращает периметр квадрата

    Пример вызова:
        square_perimeter = perimeter(6)
    '''

    a_value = int(a);

    if (a_value <= 0):
        raise ValueError("Value must be positive integers")

    return 4 * a_value

