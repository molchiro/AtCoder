A, B, C = list(map(int, input().split()))

dp = [[[0]*100 for _ in range(100)] for _ in range(100)]

def solve(dp, a, b, c):
    if a > 99 or b > 99 or c > 99:
        return 0
    elif dp[a][b][c] == 0:
        N = a+b+c
        dp[a][b][c] = ((solve(dp, a+1, b, c)+1)*a + (solve(dp, a, b+1, c)+1)*b + (solve(dp, a, b, c+1)+1)*c)/N
    return dp[a][b][c]

print(solve(dp, A, B, C))