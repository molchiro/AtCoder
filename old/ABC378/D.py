H, W, K = list(map(int, input().split()))

field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]

for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == '#':
            field[h+1][w+1] = -1

ans = 0

def move(x, y):
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

def dfs(h, w, k=0):
    global field, H, W, K, ans

    # print(*[''.join(map(str, x)) for x in field], sep='\n')
    # print()

    if field[h][w] in [1, -1]:
        return

    if k >= K:
        ans += 1
        return
    
    field[h][w] = 1

    for nh, nw in move(h, w):
        if field[nh][nw] in [1, -1]:
            continue
        dfs(nh, nw, k+1)

    field[h][w] = 0

for h in range(H):
    for w in range(W):
        dfs(h+1, w+1)


print(ans)