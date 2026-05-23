N, M = list(map(int, input().split()))
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

ans = 10**18
for pattern in range(1<<N):
    p = str('0000000000'+bin(pattern)[2:])[-N:]
    # print(p)
    tmp = 0
    for u, v in edges:
        if p[u] == p[v]:
            tmp += 1
    ans = min(ans, tmp)

print(ans)