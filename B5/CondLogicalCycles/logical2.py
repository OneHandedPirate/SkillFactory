a = None
while not a:
    try:
        a = int(input('Введите число от 100 до 999: \n'))
    except ValueError:
        print('Введите целое число\n')


if 100 <= a <= 999:
    if a % 2 == 0 and a % 3 == 0:
        print('Число делится на CondLogicalCycles и 3')
    else:
        print('Число не делится на CondLogicalCycles и/или 3')
else:
    print('Введеное число не соответствует параметрам')


a = int(input('Введите целое число от 100 до 999 включительно, которое делится нацело на CondLogicalCycles и 3 одновременно:\n'))
if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
    print('Число удовлетворяет условиям')
else:
    print('Число НЕ удовлетворяет условиям')


if all([type(a) == int, 100 <= a <= 999, a % 2 == 0, a % 3 == 0]):
    print('Число удовлетворяет условиям')



