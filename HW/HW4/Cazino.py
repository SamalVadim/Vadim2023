''' Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
 Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
В случае неудачи вывести на экран правильную комбинацию.
'''
import random

num = random.randint(1,10)
col = random.randint(1,2)
col1 = ''
print(num)
if col == 1:
    col1 = 'Черное'
else:
    col1 = 'Красное'
print(col1)

i = 1

while i < 5:
    i +=1
    variant_num = int(input('Угадай число'))# метод сплит
    variant_col = input('Угадай цвет')

    if variant_num == num and variant_col == col1:
        print('Бинго! ')
        break

    else:
        print('Пробуй еще')



print(f'Finsh! Количество попыток {i}Правильный ответ {num},{col1}')


# num = random.randint(1,10)
# col = random.randint(1,2)
# col1 = ''
# print(num)
# if col == 1:
#     col1 = 'Черное'
# else:
#     col1 = 'Красное'
# print(col1)
#
# variant_num = int(input('Угадай число'))
# variant_col = input('Угадай цвет')
#
# #count = 0
# while  variant_num != num and variant_col != col1:
# #    count += 1
#     print('Try again')
#     variant_num = int(input('Угадай число'))
#     variant_col = input('Угадай цвет')
#     print(f'Finsh! Количество попыток Правильный ответ {num},{col1}')
# print('Бинго!')


# num = random.randint(1,10)
# print(num)
#
# variant_num = int(input('Угадай число'))
#
# coun = 0
#
# while  variant_num != num:
#
#     coun += 1
#     print('Try again')
#     variant_num = int(input('Угадай число'))
#     if coun == 5:
#         break
#         print('Finish')
#
# print('Bingo')







