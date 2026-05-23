from functools import cache


N = int(input())

@cache
def f(n):
    if n == 0:
        return 1
    str_n = str(n)
    return sum([int(s) for s in str_n])

tmp = [1]
for i in range(1, N+1):
    tmp.append(sum([f(n) for n in tmp]))

print(tmp[-1])
    