N, A, X, Y = list(map(int, input().split()))

from functools import cache

@cache
def solve(n):
    global A, X, Y
    if n == 0:
        return 0

    # print(n)
    # input()
    y =  (6*Y + sum([solve(n//i) for i in range(2, 7)]))/5
    if A > 1:
        x = X + solve(n//A)
        return min(x, y)
    else:
        return y

print(solve(N))