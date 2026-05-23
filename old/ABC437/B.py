H, W, N = list(map(int, input().split()))
field = [list(map(int, input().split())) for _ in range(H)]
res = [[0]*W for _ in range(H)]
B = set()
for _ in range(N):
    b = int(input())
    B.add(b)

for h in range(H):
    for w in range(W):
        if field[h][w] in B:
            res[h][w] = 1

print(max([sum(row) for row in res]))