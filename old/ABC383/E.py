N, M, K = list(map(int, input().split()))

edges = []
for _ in range(M):
    u, v, w = list(map(lambda x: int(x) - 1, input().split()))
    edges.append((w+1, u, v))
edges.sort()
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))
A_set = set(A)
B_set = set(B)

from atcoder.dsu import DSU

dsu = DSU(N)

# 親ノードに属していてまだペアリングしていないAとB
stacks = [[[], []] for _ in range(N)]
for a in A:
    stacks[a][0].append(a)
for b in B:
    stacks[b][1].append(b)

ans = 0
for w, u, v in edges:
    if dsu.same(u, v):
        continue

    u_l = dsu.leader(u)
    v_l = dsu.leader(v)

    dsu.merge(u, v)
    if dsu.leader(u) != u_l:
        u_l, v_l = v_l, u_l
    
    stacks[u_l][0] += stacks[v_l][0]
    stacks[u_l][1] += stacks[v_l][1]
    stacks[v_l] = None

    l = dsu.leader(u_l)
    while stacks[l][0] and stacks[l][1]:
        a = stacks[l][0].pop()
        b = stacks[l][1].pop()
        ans += w

print(ans)