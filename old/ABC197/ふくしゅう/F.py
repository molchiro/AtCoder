from collections import deque

N, M = list(map(int, input().split()))

g = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = input().split()
    A = int(A)-1
    B = int(B)-1
    g[A].append((B, C))
    g[B].append((A, C))

# dp[i][j] = (0, N-1)から(i, j)に移動する最小回数。ただし0-indexed。
dp = [[float('inf')]*N for _ in range(N)]
dq = deque()
dq.append((0, N-1, 0))
while dq:
    l, r, cost = dq.popleft()
    if dp[l][r] != float('inf'):
        continue
    dp[l][r] = cost
    for next_l, next_l_C in g[l]:
        for next_r, next_r_C in g[r]:
            if next_l_C == next_r_C:
                dq.append((next_l, next_r, cost+1))

ans = float('inf')
# 偶数長
for i in range(N):
    ans = min(ans, dp[i][i]*2)
# 奇数長
for i in range(N):
    for j, _ in g[i]:
        ans = min(ans, dp[i][j]*2+1)

if ans == float('inf'):
    ans = -1

print(ans)
        