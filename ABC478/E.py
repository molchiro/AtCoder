from atcoder.scc import SCCGraph


N, Q = list(map(int, input().split()))

edges = []
vec = [[] for _ in range(N)]
for _ in range(Q):
    t, u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    edges.append((t, u, v))
    vec[u].append((t, v))


scc = SCCGraph(N)
for _, u, v in edges:
    scc.add_edge(u, v)

groups = scc.scc()
# print(groups)

# ループ内がすべてt=0かチェック
f = 1
compressed = [i for i in range(N)]
compressed_edge = [[] for _ in range(N)]
for group in groups:
    s = set(group)
    m = min(group)
    for u in group:
        compressed[u] = m
        for t, v in vec[u]:
            if v in s:
                if t == 1:
                    f = 0
            else:
                compressed_edge[m].append((t, v))

for i in range(N):
    compressed_edge[i] = [(t, compressed[v]) for t, v in compressed_edge[i]]

if f == 0:
    print('No')
    exit()

# print(compressed)
# print(compressed_edge)

# 根を見つける
tmp = [0]*N
for edges in compressed_edge:
    for t, v in edges:
        tmp[v] += 1
for i, v in enumerate(compressed):
    if i != v:
        tmp[i] += 1

roots = []
for i in range(N):
    if tmp[i] == 0:
        roots.append(i)

# print(roots)

from collections import deque
dq = deque([(1, root) for root in roots])
ans = [0]*N
while dq:
    x, u = dq.popleft()
    u = compressed[u]
    # print(dq, x, u, ans)
    if ans[u] >= x:
        continue

    ans[u] = x
    for t, v in compressed_edge[u]:
        v = compressed[v]
        if ans[v] < x+t:
            dq.append((x+t, v))

# print(ans)
for i, v in enumerate(compressed):
    ans[i] = ans[v]
tmp = min(ans)-1
ans = [x-tmp for x in ans]

if max(ans) > N:
    print('No')
    exit()


print('Yes')
print(*ans)