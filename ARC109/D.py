from collections import deque

def move(x, y, d):
    # *.
    # **
    if d == 0:
        return [[1, 1, 2], [1, 0, 1], [0, 0, 3], [1, 0, 2], [0, 0, 1], [0, 1, 2], [0, 1, 3]]
    # .*
    # **
    elif d == 1:
        return [[-1, 1, 3], [-1, 0, 0], [0, 0, 2], [-1, 0, 3], [0, 0, 0], [1, 1, 2], [1, 1, 3]]
    # **
    # .*
    elif d == 2:
        return [[-1, -1, 0], [-1, 0, 3], [0, 0, 1], [-1, 0, 0], [0, -1, 1], [0, 0, 3], [0, -1, 0]]
    # **
    # *.
    else:
        return [[1, -1, 1], [1, 0, 2], [0, 0, 0], [1, 0, 1], [0, -1, 0], [0, 0, 2], [0, -1, 1]]

cost = [[[-1]*4 for _ in range(100)] for _ in range(100)]

q = deque()
q.append([0, 0, 0])
while q:
    x, y, d = q.pop()
    c = cost[x][y][d]
    for dx, dy, nd in move(x, y, d):
        if -50 < x+dx < 50 and -50 < y+dy < 50:
            if cost[x+dx][y+dy][nd] == -1:
                cost[x+dx][y+dy][nd] = c+1
                q.append([x+dx, y+dy, nd])

T = int(input())
for _ in range(T):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    stones = [[ax, ay], [bx, by], [cx, cy]]
    stones.sort(key=lambda x: x[0]+x[1])
    