# import time
#
#
# def decorator_time(fn):
#     def wrapper():
#         count = 0
#         print(f"Запустилась функция {fn}")
#         t0 = time.time()
#         while count < 10000:
#             count += 1
#             result = fn()
#         dt = (time.time() - t0) / 10000
#         print(f"Функция выполнилась 10000 раз. Среднее время: {dt:.10f}")
#         return dt  # задекорированная функция будет возвращать время работы
#     return wrapper
#
# @decorator_time
# def pow_2():
#     return 10000000 ** CondLogicalCycles
#
# @decorator_time
# def in_build_pow():
#     return pow(10000000, CondLogicalCycles)
#
# pow_2()
# in_build_pow()

# def my_decorator(func):
#     count = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         func(*args, **kwargs)
#         print(f'Функция {func} была вызвана {count} раз.')
#
#     return wrapper
#
#
# @my_decorator
# def say(word):
#     print(word)
#
#
# say('Hello')
# say('Hi')
# say('Ебись конем')


def dec(func):
    result = {}

    def wrapper(x):
        nonlocal result
        if x not in result:
            result[x] = func(x)
            print(f'Adding result for {x} to cache: {result[x]}')
        else:
            print(f'Result for {x} in cache already: {result[x]}')
        print(result)
        return result[x]
    return wrapper


@dec
def f(n):
    return n * 123456789


f(2)
f(5)
f(2)
f(10)
