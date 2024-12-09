N = int(input())

G = [[0]*(N) for i in range(N-1)]
MG = int(input())
for _ in range(MG):
    u, v = list(map(lambda x: int(x) - 1, input().split()))
    if u > v:
        u, v = v, u
    G[u][v] = 1

MH = int(input())
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(MH)]

A = [[0]*(i+1)+list(map(int, input().split())) for i in range(N-1)]
# print(*A, sep='\n')

def solve(pattern, edge_map):
    global edges, G, MH


    H = [[0]*(N) for i in range(N-1)]
    for u, v in edges:
        u, v = edge_map[u], edge_map[v]
        if u > v:
            u, v = v, u
        # print(u, v)
        H[u][v] = 1


    # print(*H, sep='\n')

    res = 0

    for i in range(N-1):
        for j in range(N):
            if G[i][j] == H[i][j]:
                continue
            a, b = pattern[i], pattern[j]
            if a > b:
                a, b = b, a
            # print(a, b)
            res += A[a][b]

    return res

from itertools import permutations

ans = float('inf')

for pattern in permutations(range(N)):
    edge_map = {u: i for i, u in enumerate(pattern)}
    # print(pattern, edge_map)
    ans = min(ans, solve(pattern, edge_map))

print(ans)