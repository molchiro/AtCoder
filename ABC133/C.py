L, R = list(map(int, input().split()))

x = []
for i in range(2019):
    for j in range(L//2019, R//2019+1):
        tmp = 2019*j + i
        if tmp >= L and tmp <= R:
            x.append(i)
            break

from itertools import combinations

pairs = list(combinations(x, 2))
print(min([(p[0]*p[1])%2019 for p in pairs]))
