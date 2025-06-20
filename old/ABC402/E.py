import sys
sys.setrecursionlimit(10**9)

N, X = list(map(int, input().split()))
problems = [list(map(int, input().split())) for _ in range(N)]

from functools import cache

# x円使用済みで、状態がj
@cache
def solve(x, j):
    global N, X, problems
    res = 0
    # i番目の問題に挑戦する
    for i in range(N):
        s, c, p = problems[i]
        p /= 100
        if x+c > X:
            continue
        if (j>>i) & 1:
            continue

        res = max(res, (solve(x+c, j+(1<<i))+s)*p + solve(x+c, j)*(1-p))

    return res

# 深い再帰を起こさないために後ろからループさせておく
for i in range(5000):
    for j in range(1<<N, -1, -1):
        solve(i, j)
print(solve(0, 0))