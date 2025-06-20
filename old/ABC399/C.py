N, M = list(map(int, input().split()))

from atcoder.dsu import DSU
dsu = DSU(N)

ans = 0
for _ in range(M):
    u, v = list(map(lambda x: int(x) - 1, input().split()))
    if dsu.same(u, v):
        ans += 1
    else:
        dsu.merge(u, v)
print(ans)