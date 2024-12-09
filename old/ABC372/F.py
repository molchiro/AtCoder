MOD = 998244353

N, M, K = list(map(int, input().split()))
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
edges.append([N-1, 0])


inline_dp = [0]*(N+K)
offset = K
inline_dp[offset] = 1
# print(inline_dp)
for _ in range(K):
    stack = []
    for x, y in edges:
        stack.append((y, inline_dp[offset+x]))
    offset -= 1
    for dest, value in stack:
        inline_dp[dest+offset] += value
        inline_dp[dest+offset] %= MOD
    # print(inline_dp)

ans = 0
for i in range(N):
    ans += inline_dp[i]
    ans %= MOD
print(ans)