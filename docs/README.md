# Библиотека для операций над геометрическими фигурами
```
В данной библиотеке реализованы функции рассчёта периметра и площади круга, прямоугольника и квадрата
```

## Треугольник

**Для треугольника реализованы функции `area` и `perimeter`**

### Area
Эта функция принимает высоту и основание треугольника и возвращает его площадь
```python
def area(a, h): return (a * h) / 2 
```
**Пример вызова**
```python
a = 10
h = 12

triangle_area = area(a, h) # 60
```

### Perimeter
Эта функция принимает стороны треугольника и возвращает его периметр

```python
def perimeter(a, b, c): return a + b + c
```

**Пример вызова**
```python
a = 3
b = 4
c = 5

triangle_perimeter = perimeter(a, b, c) # 12
```

## Квадрат

**Для квадрата реализованы функции `area` и `perimeter`**

### Area
Эта функция принимает сторону квадрата и возвращает его площадь
```python
def area(a): return a * a
```
**Пример вызова**
```python
a = 10

square_area = area(a) # 100
```

### Perimeter
Эта функция принимает сторону квадрата и возвращает его периметр

```python
def perimeter(a): return 4 * a
```

**Пример вызова**
```python
a = 3

square_perimeter = perimeter(a) # 12
```

## Прямоугольник

**Для прямоугольника реализованы функции `area` и `perimeter`**

### Area
Эта функция принимает высоту и ширину прямоугольника и возвращает его площадь
```python
def area(a, b): return a * b
```
**Пример вызова**
```python
a = 10
b = 5

rectangle_area = area(a, b) # 50
```

### Perimeter
Эта функция принимает высоту и ширину прямоугольника и возвращает его периметр

```python
def perimeter(a, b): return (a + b) * 2
```

**Пример вызова**
```python
a = 3
b = 4

rectangle_perimeter = perimeter(a, b) # 14
```

## Круг

**Для круга реализованы функции `area` и `perimeter`**

### Area
Эта функция радиус круга и возвращает его площадь
```python
def area(r): return math.pi * r * r
```
**Пример вызова**
```python
r = 10

circle_area = area(r) # 314.1592653589793
```

### Perimeter
Эта функция принимает радиус окружности и возвращает её длину

```python
def perimeter(r): return 2 * math.pi * r
```

**Пример вызова**
```python
r = 3

circle_perimeter = perimeter(r) # 18.84955592153876
```

# Changelog

### Commit
```
Hash - 81ca9d0142bf750337f5ef91cda8e2f9ccb93e63
Date - Wed Sep 18 12:27:12 2024 +0300
Message - new file rectangle.py
```

### Commit
```
Hash - fc35fda2ccb5eb7ce5205acdf4d6dbff756f9c5b
Date - Wed Sep 18 12:28:18 2024 +0300
Message - fixed rectangle.py
```