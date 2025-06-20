from collections import deque

H, W, D = list(map(int, input().split()))
D += 1
dq = deque()
field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == '#':
            field[h+1][w+1] = -1
        elif S[w] == 'H':
            dq.append((h+1, w+1, D))

# print(*field, sep='\n')

def move(x, y):
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

while dq:
    h, w, d = dq.popleft()

    if field[h][w] > d:
        continue

    field[h][w] = d

    if d-1 == 0:
        continue
    
    for h_n, w_n in move(h, w):
        if field[h_n][w_n] == -1:
            continue

        dq.append((h_n, w_n, d-1))

ans = 0
for h in range(H+2):
    for w in range(W+2):
        if field[h][w] > 0:
            ans += 1


print(ans)
