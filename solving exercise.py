'''Функция sqrt() извлекает квадратный корень
from math import sqrt
Узнаем у пользователя, корни какого конкретного уравнения мы будем искать.
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))'''

from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

#a ** 2 + 2 * a * b + b ** 2 == 0

D = b ** 2 - 4 * a * c
print(f'Дискриминант равен {D}')
if D > 0:
    print('x1 =',(-b + sqrt(D)) / (2 * a), 'x2 =',(-b - sqrt(D)) / (2 * a))

elif D == 0:
    print(-b/(2*a))
else:
    print('Корней нет')
