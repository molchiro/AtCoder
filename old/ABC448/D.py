from atcoder.segtree import SegTree

N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

kind = sorted(list(set(A)))
d = {v: i for i, v in enumerate(kind)}


import sys
sys.setrecursionlimit(10**9)

seg = SegTree(lambda x, y: max(x, y), 0, N)
seen = [0]*N
seen[0] = 1
ans = [None]*N
ct = [0]*len(kind)
f = 0

def dfs(u):
    global N, A, G
    global seg, seen, ans, ct, f

    a = A[u]
    idx = d[a]
    if ct[idx] == 1:

        ct[idx] += 1
        seg.set(idx, 1)
    else:
        ct[idx] += 1

    ans[u] = 'Yes' if seg.all_prod() else 'No'
    seen[u] = 1

    for v in G[u]:
        if seen[v]:
            continue
        seen[v] = 1
        dfs(v)
    
    if ct[idx] == 2:
        ct[idx] -= 1
        seg.set(idx, 0)
    else:
        ct[idx] -= 1

dfs(0)

print(*ans, sep='\n')