strng = input()

last = strng[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку


for c in strng:
    if c == last:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += last + str(count)  # иначе - записываем в результат
        last = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += last + str(count)  # и добавляем в результат последний символ
print(result)
