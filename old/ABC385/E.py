from collections import defaultdict

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

ans = N
for i in range(N):
    dd = defaultdict(int)
    for c in G[i]:
        g_n = len(G[c])-1
        dd[g_n] += 1
    
    keys = list(dd.keys())
    if keys == [0]:
        # print('debug', 'no grand children')
        continue
    
    keys.sort(reverse=True)
    tmp = 0
    accum = 0
    for k in keys:
        accum += dd[k]
        tmp = max(tmp, accum + k*accum)
    ans = min(ans, N-(1+tmp))
print(ans)