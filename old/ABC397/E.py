N, K = list(map(int, input().split()))

G = [[] for _ in range(N*K)]
for _ in range(N*K-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

# 頂点0を根とする木を構築
c = [set() for _ in range(N*K)]
p = [-1]*(N*K)

from collections import deque

dq = deque()
dq.append(0)
seen = [0]*(N*K)
while dq:
    u = dq.pop()
    if seen[u]:
        continue
    seen[u] = 1

    for v in G[u]:
        if seen[v]:
            continue
        c[u].add(v)
        p[v] = (u)
        dq.append(v)

# print(c)
# print(p)

c_rem = [len(x) for x in c] # 未確定の子の数

# 葉から順にパスが作れるか確認
dp = [-1]*(N*K)
dq = deque([i for i, n in enumerate(c_rem) if n == 0])
while dq:
    u = dq.popleft()
    # print(u, dp)

    if c_rem[u] > 0:
        continue

    # 大きさが1以上の子を抽出
    valid_children = []
    for v in c[u]:
        if dp[v] > 0:
            valid_children.append(v)

    if len(valid_children) == 0:
        dp[u] = 1
        if dp[u] == K:
            dp[u] = 0
    elif len(valid_children) == 1:
        dp[u] = dp[valid_children[0]] + 1
        if dp[u] == K:
            dp[u] = 0
    elif len(valid_children) == 2:
        dp[u] = dp[valid_children[0]] + dp[valid_children[1]] + 1
        if dp[u] == K:
            dp[u] = 0
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()

    if u != 0:
        c_rem[p[u]] -= 1
        dq.append(p[u])

print('Yes')