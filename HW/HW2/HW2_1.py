''' Задача №1: Определить, является ли год високосным
'''
import math

# year = int(input('Введите год:'))
# if year % 400 == 0:
#     print('Год високосный')
# elif year % 100 == 0:
#     print('Год високосный')
# elif year% 4 == 0:
#     print('Год високосный')
# else:
#     print('Год невисокосный')

'''Задача №2: Определить существование треугольника и его тип
'''
# a = int(input('Сторона А:'))
# b = int(input('Сторона В:'))
# c = int(input('Сторона С:'))
# if a+b > c and b+c>a and c+a>b:
#     print('Треугольник существует')
#     if a==b or b==c or c==a:
#         print('Треугольник равнобедренный')
#         if a == b == c:
#             print('Треугольник равносторонний')
# else:
#     print('Треугольник не существует')


# a = int(input('Угол А:'))
# b = int(input('Угол В:'))
# c = int(input('Угол С:'))
# if a + b + c == 180:
#     print('Треугольник сущесвует')
#     if a == b or b == c or c == a:
#         print('Треугольник равнобедренный')
#         if a == 45 or b == 45 or c == 45:
#             print('Треугольник равнобедренный прямоугольный')
#         if a == b == c:
#             print('Треугольник равносторонний')
#     elif a == 90 or b == 90 or c == 90:
#         print('Треугольник прямоугольный')
# else:
#     print('Треугольник не существует')


''' Задача №3: Определить принадлежность точки кругу с 
центром в начале координат. 
Вводятся координаты (x,y) точки и радиус круга r. 
Определить принадлежит ли данная точка кругу, если 
его центр находится в начале координат.
'''
x = int(input('Введите координату X: '))
y = int(input('Введите координату Y:'))
r_circle = int(input('Введите длинну радиуса окружности:'))

if r_circle**2 == math.pow(x,2) + math.pow(y,2):
    print('Принадлежит')
else:
    print('Не принадлежит')





