from functools import cache

N = int(input())
A = list(map(int, input().split()))

@cache
def f(l, r):
    print(l, r)
    if r-l <= 2:
        return A[l] + A[l+1]
    return min([f(l, i) + f(i, r) for i in range(l+1, r)])

print(f(0, N))