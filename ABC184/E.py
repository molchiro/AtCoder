from collections import deque

H, W = list(map(int, input().split()))
field = [[-1]*(W+2)] + [[-1]+ [float('inf')]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
teleporter = [['']*(W+2)] + [['']*(W+2) for _ in range(H)] + [['']*(W+2)]
teleport_to = { chr(ord('a')+i): [] for i in range(26) }

for i in range(H):
    s = input()
    for j in range(W):
        c = s[j]
        if c == '#':
            field[i+1][j+1] = -1
        elif c == '.':
            continue
        elif c == 'S':
            S = [i+1, j+1]
        elif c == 'G':
            G = [i+1, j+1]
        else:
            teleporter[i+1][j+1] = c
            teleport_to[c].append([i+1, j+1])

q = deque()
q.append(S)
field[S[0]][S[1]] = 0

while q:
    h, w = q.popleft()
    cost = field[h][w] + 1

    move_to = [[h+1, w], [h-1, w], [h, w+1], [h, w-1]]
    if teleporter[h][w]:
        move_to += teleport_to[teleporter[h][w]]
        teleport_to[teleporter[h][w]] = []
    
    for h_, w_ in move_to:
        if cost < field[h_][w_]:
            field[h_][w_] = cost
            q.append([h_, w_])
    
ans = field[G[0]][G[1]]
print(ans if ans != float('inf') else -1)