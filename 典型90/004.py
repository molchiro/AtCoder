H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
hrz = [sum(A[i]) for i in range(H)]
vrt = [sum([A[i][j] for i in range(H)]) for j in range(W)]
for h in range(H):
    print(*[vrt[w] + hrz[h] - A[h][w] for w in range(W)])