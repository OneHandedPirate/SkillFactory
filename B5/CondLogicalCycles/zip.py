L = [1, 2, 4, 5]
M = [2, 5, 5, 6, 6]

N = [a*b for a, b in zip(L, M, strict=True)]
print(N)

j = zip(L, M)
print(j)