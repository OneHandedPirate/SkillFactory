def min_lst(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_lst(L[1:]) else min_lst(L[1:])

l = [1, 4, 0, -1, 5]
print(min_lst(l))


def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res

print(mirror(123))


def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10) 