from collections import deque


N, K = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

V = list(map(lambda x: int(x) - 1, input().split()))
V_set = set(V)

# bfsしつつ、Vに含まれるノードを見つけたら根まで遡る
p = [-1]*N
s = V[0]
p[s] = s
dq = deque([s])
seen = [0]*N
ans = [0]*N
# ans[s] = 1
while dq:
    u = dq.popleft()
    # print(u)

    if seen[u]:
        continue
    seen[u] = 1

    for v in G[u]:
        if seen[v]:
            continue
        dq.append(v)
        p[v] = u

    if u in V_set:
        while ans[u] == 0:
            ans[u] = 1
            u = p[u]

print(sum(ans))