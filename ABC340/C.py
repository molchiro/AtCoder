from functools import cache

N = int(input())


@cache
def culc(x):
    if x == 1:
        return 0
    else:
        return x + culc(x//2) + culc(x-x//2)

print(culc(N))