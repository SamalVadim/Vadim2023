''' Задача:
Вычислить сумму цифр случайного трёхзначного числа
'''
from random import randint

a = randint(0, 999)
a1 = a // 100
a2 = a % 10
a3 = a % 100 // 10
s = a1 + a2 + a3
print(a1, a2, a3, s)
