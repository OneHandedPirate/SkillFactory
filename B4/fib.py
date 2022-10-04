# def fib():
#     a, b = 0, 1
#     yield a
#     yield b
#
#
# a = fib()
# b = fib()
# print(id(a), id(b))

# def fibonacci(xterms):
#     # первые два условия
#     x1 = 0
#     x2 = 1
#     count = 0
#
#     if xterms <= 0:
#         print("Укажите целое число больше 0")
#     elif xterms == 1:
#         print("Последовательность Фибоначчи до", xterms, ":")
#         print(x1)
#     else:
#         while count < xterms:
#             xth = x1 + x2
#             x1 = x2
#             x2 = xth
#             count += 1
#             yield xth
#
#
# fib = fibonacci(5)
#
# for i in fib:
#     print(i)


# def fib(n):
#     a, b = 0, 1
#     for i in range(n-1):
#         a, b = b, a + b
#     return a
#
# print(fib(100000))

a = [1, 2, 3]


