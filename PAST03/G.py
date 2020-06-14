from collections import deque

def forward(now):
    x, y = now
    return [(x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x, y-1)]

def backward(now):
    x, y = now
    return [(x+1, y), (x+1, y-1), (x, y+1), (x-1, y-1), (x-1, y), (x, y-1)]

INF = 1001001001

N, X, Y = list(map(int, input().split()))
blocks = {tuple(map(int, input().split())) for _ in range(N)}

S = (1600, 1600)
G = (1600+X, 1600+Y)
table = [[INF for _ in range(3200)] for _ in range(3200)]
table[S[0]][S[1]] = 0
table[G[0]][G[1]] = -1
for sq in blocks:
    table[1600+sq[0]][1600+sq[1]] = None

S_queue = deque()
G_queue = deque()
S_queue.append(S)
G_queue.append(G)
S_dist = 0
G_dist = -1
switch = 'S'
solved = False
while solved == False and S_queue and G_queue:
    if switch == 'S':
        if table[S_queue[0][0]][S_queue[0][1]] > S_dist:
            S_dist += 1
            switch = 'G'
            continue
        now = S_queue.popleft()
        next_squares = forward(now)
        for sq in next_squares:
            x = sq[0]
            y = sq[1]
            if table[x][y] == INF:
                table[x][y] = S_dist + 1
                S_queue.append(sq)
            elif table[x][y] == None:
                continue
            elif table[x][y] < 0:
                solved = True
                break
    else:
        if table[G_queue[0][0]][G_queue[0][1]] < G_dist:
            G_dist -= 1
            switch = 'S'
            continue
        now = G_queue.popleft()
        next_squares = backward(now)
        for sq in next_squares:
            x = sq[0]
            y = sq[1]
            if table[x][y] == INF:
                table[x][y] = G_dist - 1
                G_queue.append(sq)
            elif table[x][y] == None:
                continue
            elif table[x][y] > 0:
                solved = True
                break

if solved:
    ans = S_dist - G_dist
    print(ans)
else:
    print(-1)