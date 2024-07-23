N, Q = list(map(int, input().split()))

from atcoder.dsu import DSU

DSUs = [DSU(N) for _ in range(10)]

ans = 0
for _ in range(N-1):
    a, b, c = list(map(lambda x: int(x) - 1, input().split()))
    ans += c+1
    for i in range(c, 10):
        DSUs[i].merge(a, b)

for _ in range(Q):
    u, v, w = list(map(lambda x: int(x) - 1, input().split()))
    if not DSUs[w].same(u, v):
        for i in range(w, 10):
            if DSUs[i].same(u, v):
                ans -= (i-w)
                break
            DSUs[i].merge(u, v)
    print(ans)