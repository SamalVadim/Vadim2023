''' Задание №2
Найти площадь и периметр прямоугольного треугольника
Примечание: В данном решении используйте модуль math.'''

import math
cat1 = int(input())
cat2 = int(input())
gip1 = cat1**2+cat2**2
print(gip1)
gip = math.sqrt(gip1)
print(gip)
P = cat1+cat2+gip
S = cat1*cat2/2
print(P)



