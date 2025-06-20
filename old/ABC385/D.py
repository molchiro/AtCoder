from sortedcontainers import SortedList
from collections import defaultdict

N, M, sx, sy = list(map(int, input().split()))

houses_h = defaultdict(SortedList)
houses_w = defaultdict(SortedList)
for _ in range(N):
    x, y = list(map(int, input().split()))
    houses_h[y].add(x)
    houses_w[x].add(y)

ans = 0

def culc_v(x, u, v):
    global houses_h, houses_w
    global ans

    l = houses_w[x].bisect_left(u)
    r = houses_w[x].bisect_right(v)
    stack = []
    for i in range(l, r):
        stack.append(houses_w[x][i])
        ans += 1
    for y in stack:
        houses_w[x].pop(houses_w[x].bisect_left(y))
        houses_h[y].pop(houses_h[y].bisect_left(x))

def culc_h(y, u, v):
    global houses_h, houses_w
    global ans

    l = houses_h[y].bisect_left(u)
    r = houses_h[y].bisect_right(v)
    stack = []
    for i in range(l, r):
        stack.append(houses_h[y][i])
        ans += 1
    for x in stack:
        houses_w[x].pop(houses_w[x].bisect_left(y))
        houses_h[y].pop(houses_h[y].bisect_left(x))

for _ in range(M):
    # print('debug', houses_h)
    # print('debug', houses_w)
    D, C = input().split()
    C = int(C)

    if D in ['U', 'D']:
        if D == 'D':
            nxt_sy = sy-C
            culc_v(sx, nxt_sy, sy)
        else:
            nxt_sy = sy+C
            culc_v(sx, sy, nxt_sy)
        sy = nxt_sy
    else:
        if D == 'L':
            nxt_sx = sx-C
            culc_h(sy, nxt_sx, sx)
        else:
            nxt_sx = sx+C
            culc_h(sy, sx, nxt_sx)
        sx = nxt_sx
print(sx, sy, ans)