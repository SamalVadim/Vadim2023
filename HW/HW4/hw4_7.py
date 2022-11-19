''' Массив из 7 цифр. Если четных цифр в нем больше чем нечетных,
то найти сумму всех его цифр, если нечетных больше,
то найти произведение 1 3 и 6 элемента.
'''

a = [1,2,3,4,5,6,7]
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
        print(even)
    else:
        odd.append(i)
        print(odd)
if even > odd:
    print(sum(a))
else:
    print(a[1]*a[3]*a[6])

