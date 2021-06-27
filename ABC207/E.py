import sys
sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(int, input().split()))

dp = [[None]*(N+1) for _ in range(N+1)]
def solve(i, j):
    if dp[i][j] == None:
        dp[i][j] = 0
        tmp = 0
        for k in range(i+1, N+1):
            tmp += A[k-1]
            if tmp%(j+1) == 0:
                if k == N:
                    dp[i][j] += 1
                else:
                    dp[i][j] += solve(k, j+1)
                dp[i][j] %= 10**9+7
    return dp[i][j]
print(solve(0, 0))
# print(dp)