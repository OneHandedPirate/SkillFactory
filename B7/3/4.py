try:
    s = int(input('Введите число:\n'))
except ValueError:
    print('Вы ввели не число')
else:
    print(f'Вы ввели число {s}')
finally:
    print('Выход из программы')
