''' 1. Перемножить все нечётные значения в диапазоне от 1 до 100.
'''
# a = list(range(1, 100))
# p = 1
# for i in a:
#     if i % 2 != 0:
#         p *= i
#
# print(p)

''' Записать в массив все числа в диапазоне от 1 до 500 кратные 5.
'''
# a = list(range(0,501,5))
# print(a)


# a = list(range(0,501))
# a1 = []
# for i in a:
#     if i %5 == 0:
#         a1.append(i)
# print(a1)

''' 3. Вывести на экран все чётные значения в диапазоне от 1 до 497.
'''
# a = list(range(2,498,2))
# print(a)

# a = list(range(1,497))
# for i in a:
#     if i % 2 ==0:
#         print(i)

'''Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив.
'''
a = [1,2,4,1,5,2,3,6,1,5,8,2,4,3,6,9]
# a1 = []
# for i in a:
#      if a.count(i) >=2:
#          print(i)






# ''' Таблица умножения от 1 до 9'''
# a = list(range(1,10))
# b = list(range(1,10))
# for i in a:
#     for j in b:
#         tab = i*j
#         print(tab)
#         for i in range(len(tab)):
#             if i >10:
#                 print()
''' Калькулятор '''

while True:
    z = input('Хотите выполнить вычисления? Ввелите: Да или Нет'  )
    if z == 'Нет':
        print('Закончить цикл')
        break
    a = float(input('Введите первое число'))
    z = input('Введите операцию: +, -, *, /,^')
    b = float(input('Введите второе число'))
    if z != '/' and z != '*' and z != '-' and z != '+':
        print('Невернный символ ')
    elif z == '/':
        if b == 0:
            print('На 0 делить нельзя')
        else:
            print(a/b)
    elif z == '*':
        print(a * b)
    elif z == '+':
        print(a + b)
    elif z == '-':
        print(a - b)
    elif z == '^':
        print(a ** b)