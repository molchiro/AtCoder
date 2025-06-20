H, W = list(map(int, input().split()))
buildings = [[] for _ in range(10**6)]
F = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(H)]
for h in range(H):
    for w in range(W):
        f = F[h][w]
        buildings[f].append((h, w))

Q = int(input())
queries = []
for i in range(Q):
    A,B,Y,C,D,Z = list(map(lambda x: int(x) - 1, input().split()))
    if Y < Z:
        C,D,Z = A,B,Y
    queries.append((i, A,B,Y,C,D,Z))
queries.sort()


from atcoder.dsu import DSU

dsu = DSU(H*W)

