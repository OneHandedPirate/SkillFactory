last = 0
def e():
    n = 1
    while True:
        yield (1 + 1 / n) ** n
        print(n)
        n += 1


for a in e():  # e() - генератор
    if (a - last) < 0.00000001: # ограничение на точность
        print(a)
        break  # после достижения которого - завершаем цикл
    else:
        last = a  # иначе - присваиваем новое значение

