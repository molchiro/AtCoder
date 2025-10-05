N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

from math import gcd

from collections import defaultdict

dd = defaultdict(dict)
for i in range(N-1):
    for j in range(i+1, N):
        p1 = points[i]
        p2 = points[j]

        if p2[0] < p1[0]:
            p1, p2 = p2, p1

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        # print(i, j, p1, p2, dx, dy)

        if dx == 0:
            if abs(dy) in dd[(0, 1)].keys():
                dd[(0, 1)][abs(dy)] += 1
            else:
                dd[(0, 1)][abs(dy)] = 1
        elif dy == 0:
            if abs(dx) in dd[(1, 0)].keys():
                dd[(1, 0)][abs(dx)] += 1
            else:
                dd[(1, 0)][abs(dx)] = 1
        else:
            a = gcd(abs(dx), abs(dy))
            dx //= a
            dy //= a
            if a in dd[(dx, dy)].keys():
                dd[(dx, dy)][a] += 1
            else:
                dd[(dx, dy)][a] = 1


# print(dd)

ans = 0
tmp = 0

for d in dd.values():
    accum = 0
    for c in d.values():
        accum += c
        tmp += c*(c-1)//2
    ans += accum*(accum-1)//2
ans -= tmp//2
print(ans)