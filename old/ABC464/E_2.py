H, W, Q = list(map(int, input().split()))

imos = [[-1]*(W+1) for _ in range(H+1)]
d = dict()
for i in range(Q):
    R, C, X = input().split()
    imos[int(R)-1][int(C)-1] = i
    d[i] = X
d[-1] = 'A'

for h in range(H-1, -1, -1):
    for w in range(W-1, -1, -1):
        imos[h][w] = max(imos[h][w], imos[h+1][w], imos[h][w+1])

for h in range(H):
    for w in range(W):
        print(d[imos[h][w]], end='')
    print()