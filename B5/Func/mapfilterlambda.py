L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(len, L)))

# def even(x):
#     return x % 2 == 0
#
#
# print(list(filter(even, [-2, -1, 0, 1, -3, 2, -3])))

data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]

srtdt = sorted(data, key=lambda x: x[0] / x[1] ** 2)
print(srtdt)

print(min(data, key=lambda x: x[0] / x[1] ** 2))