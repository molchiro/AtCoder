N, M = list(map(int, input().split()))

Q = []
S = []

for i in range(M):
    K, C = list(map(int, input().split()))
    Q.append((C, i, K))
    S.append(list(map(lambda x: int(x) - 1, input().split())))

Q.sort()

from atcoder.dsu import DSU

ans = 0
uf = DSU(N)
for c, i, k in Q:
    s = S[i]
    for j in range(k-1):
        u, v = s[j], s[j+1]
        if uf.same(u, v):
            continue
        
        ans += c
        uf.merge(u, v)

if uf.size(0) == N:

    print(ans)
else:
    print(-1)