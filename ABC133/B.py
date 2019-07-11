N, D = list(map(int, input().split()))
X = [list(map(int, input().split())) for i in range(N)]

from itertools import combinations

pairs = list(combinations(X, 2))

res = 0
for pair in pairs:
    d = 0
    for i in range(D):
        d += (pair[0][i] - pair[1][i])**2
    d = d**0.5
    if int(d) == d:
        res += 1

print(res)