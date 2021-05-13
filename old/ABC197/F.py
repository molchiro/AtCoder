from collections import deque

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = input().split()
    A = int(A)-1
    B = int(B)-1
    graph[A].append((B, C))
    graph[B].append((A, C))

# dp[l: left_node][r: right_node] = node(0, N-1)のペアから出発して(l, r)のペアに至る最小cost
dp = [[float('inf')]*N for _ in range(N)]

# (left_node, right_node, cost)
d = deque()
d.append((0, N-1, 0))
while d:
    l, r, c = d.popleft()
    if dp[l][r] != float('inf'):
        continue
    dp[l][r] = c
    for next_l, chr_l in graph[l]:
        for next_r, chr_r in graph[r]:
            if chr_l == chr_r:
                d.append((next_l, next_r, c+1))

# search answer
ans = float('inf')
# 偶数長
for i in range(N):
    ans = min(ans, dp[i][i]*2)
# 奇数長
for i in range(N):
    for j, _ in graph[i]:
        ans = min(ans, dp[i][j]*2+1)

if ans == float('inf'):
    ans = -1
print(ans)