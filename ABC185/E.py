import sys

sys.setrecursionlimit(10**9)

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[float('inf')]*1001 for _ in range(1001)]

def solve(i, j):
    if i == 0:
        dp[0][j] = j
    if j == 0:
        dp[i][0] = i
    if dp[i][j] == float('inf'):
        dp[i][j] = min(dp[i][j], solve(i-1, j) + 1)
        dp[i][j] = min(dp[i][j], solve(i, j-1) + 1)
        dp[i][j] = min(dp[i][j], solve(i-1, j-1) + (0 if A[i-1] == B[j-1] else 1))
    return dp[i][j]

print(solve(N, M))        