H, W = list(map(int, input().split()))
field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
for h in range(H):
    A = input()
    for w in range(W):
        x = A[w]
        if x == '#':
            field[h+1][w+1] = -1
        elif x == 'o':
            field[h+1][w+1] = 1
        elif x == 'x':
            field[h+1][w+1] = 2
        elif x == '?':
            field[h+1][w+1] = 3
        elif x == 'S':
            start = (h+1, w+1)
        elif x == 'G':
            goal = (h+1, w+1)

dist = [[[10**18]*2 for _ in range(W+2)] for _ in range(H+2)]
dist[start[0]][start[1]][0] = 0

from collections import deque

dq = deque()
dq.append((start[0], start[1], 0))

while dq:
    h, w, f = dq.popleft()
    d = dist[h][w][f]

    for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nh = h + dh
        nw = w + dw
        if field[nh][nw] == -1:
            continue
        elif field[nh][nw] == 0:
            if dist[nh][nw][f] == 10**18:
                dist[nh][nw][f] = d+1
                dq.append((nh, nw, f))
        elif field[nh][nw] == 1:
            if f == 1:
                continue
            if dist[nh][nw][f] == 10**18:
                dist[nh][nw][f] = d+1
                dq.append((nh, nw, f))

        elif field[nh][nw] == 2:
            if f == 0:
                continue
            if dist[nh][nw][f] == 10**18:
                dist[nh][nw][f] = d+1
                dq.append((nh, nw, f))
        elif field[nh][nw] == 3:
            if dist[nh][nw][(f+1)%2] == 10**18:
                dist[nh][nw][(f+1)%2] = d+1
                dq.append((nh, nw, (f+1)%2))

ans = min(dist[goal[0]][goal[1]])
if ans == 10**18:
    ans = -1
print(ans)
