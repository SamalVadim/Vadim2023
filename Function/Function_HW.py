''' Написать функцию is_year_leap, принимающую 1 аргумент — год,
и возвращающую True, если год високосный, и False иначе.
'''

# def is_year_leap(year):
#
#
#     if year % 400 == 0 and year % 100 == 0:
#         print('Високосный')
#     elif year % 4 == 0:
#         print('Високосный')
#     else:
#         print(" Не високосный")
#
#
# is_year_leap(int(input()))

''' Написать функцию square, принимающую 1 аргумент — сторону квадрата, 
и возвращающую 3 значения (с помощью кортежа): периметр квадрата, 
площадь квадрата и диагональ квадрата. Сторону квадрата вводить с клавиатуры. 
'''
# import math
# def squar(a):
#     b = 4*a, a**2, math.sqrt(a**2*2)
#
#     return b
#
# b = squar(float(input()))
# print(b, type(b))
# for i in range(len(b)):
#     s = b[0]
#     d = b[1]
#     f = b[2]
# print(f'периметр квадрата = {s},площадь квадрата = {d} и диагональ квадрата = {f}')


''' Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень). 
Номер месяца вводить с клавиатуры.
'''
# def seasons(a):
#
#     if 0< a< 13:
#         if 3 <= a < 6:
#             print('Весна')
#         elif 6 <= a < 9:
#             print('Лето')
#         elif 9 <= a < 12:
#             print('Осень')
#         else:
#             print('Зима')
#     else:
#         print('Неверный номер месяца')
#
#
#
# seasons(int(input()))


''' Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, 
и возвращающую True, если оно простое, и False - иначе.
'''
# def is_prime(x):
#     a = []
#     for i in range(2,(x-1)):
#         if x % i == 0:
#             a.append(i)
#     res = False if len(a)!= 0 else True  #''' аналог записи if len(a) != 0: /n return False /n else: /n return True'''
#     return res
#
#
# b = int(input())
# print(is_prime(b))

''' Функция, вычисляющая среднее арифметическое элементов массива. 
Массив должен состоять из случайных чисел, длинной 10 элементов. 
'''
# from random import randint
# def get_avar(a):
#     s = sum(a)/len(a)
#     return s, sum(a), len(a)
#
# x = [randint(1,20) for i in range(1,11)]
# print(get_avar(x))


''' Простейший калькулятор c введёнными двумя числами вещественного типа. 
Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.  
Обработать ошибку: “Деление на ноль” 
Ноль использовать в качестве завершения программы (сделать как отдельную операцию). 
'''


def oper(x):
    try:
        if x == '+':
            rez = num + num2
        if x == '-':
            rez = num - num2
        if x == '*':
            rez = num * num2
        if x == '/':
            rez = num / num2
        return rez
    except ZeroDivisionError:
        print('Devision by zero')


while True:
    num = int(input())
    if num == 0:
        print('Calculation is over')
        break
    num2 = int(input())
    operation = input()
    oper(operation)


    print(oper(operation))
