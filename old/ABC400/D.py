H, W = list(map(int, input().split()))
field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
for h in range(H):
    C = input()
    for w in range(W):
        if C[w] == '#':
            field[h+1][w+1] = -1

A,B,C,D = list(map(int, input().split()))
start = (A, B)
goal = (C, D)

from collections import deque

dq = deque()
dq.append((start, 0))
seen = set()
while dq:
    u, d = dq.popleft()
    if u == goal:
        print(d)
        exit()
    if u in seen:
        continue

    h, w = u
    if not 1 <= h <= H:
        continue
    if not 1 <= w <= W:
        continue
    
    
    seen.add(u)
    for dh, dw in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if field[h+dh][w+dw] == -1:
            dq.append(((h+dh, w+dw), d+1))
            dq.append(((h+dh+dh, w+dw+dw), d+1))
        else:
            dq.appendleft(((h+dh, w+dw), d))



