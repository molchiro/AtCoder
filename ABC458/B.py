H, W = list(map(int, input().split()))

field = [[0]*(W+2)] + [[0]+ [1]*W + [0] for _ in range(H)] + [[0]*(W+2)]

ans = [[] for _ in range(H)]

for h in range(H):
    for w in range(W):
        ans[h].append(field[h+1][w] + field[h+1][w+2] + field[h][w+1] + field[h+2][w+1])

for row in ans:
    print(*row)