# a = 0
# b = 0
#
# while id(a) == id(b):
#     a += 1
#     b += 1
#
# print(a)

# c = 1234567890000000
# d = 1234567890000000
#
# print(c == d)
# # True
#
# print(c is d)
# print(id(c), id(d))
# # False

# L = ['Hello', 'world']
# M = L.copy()
#
# L.append('!')
# print(M)

text = input('Введите текст:\n')

print(len(set(text)))