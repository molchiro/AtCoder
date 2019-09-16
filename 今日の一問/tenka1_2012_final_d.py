import itertools
import time
def triangle_S(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    return abs((x1-x3)*(y2-y3) - (x2-x3)*(y1-y3))/2


N = int(input())
P = [list(map(int, input().split())) for i in range(N)]

M = 0
# [triangle, remainds, S]
res = [[[], list(range(N)), 0]]

start_t = time.time()

while len(res[0][1]) > 0 and time.time() - start_t < 1.9:
    tmp = []
    for A in res:
        for triangle in list(itertools.combinations(A[1],3)):
            s = triangle_S(P[triangle[0]], P[triangle[1]], P[triangle[2]])
            if s == 0:
                continue
            tmp.append([A[0] + [list(triangle)], [x for x in A[1] if not x in triangle], A[2] + s])
    res = tmp

ans = max(res, key=lambda x: x[2])[0]
for tri in ans:
    print(*tri)