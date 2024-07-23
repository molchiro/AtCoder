T = input()
N = int(input())

# dp[i]: i文字目まで一致している時の最小コスト

inf = 10**18
dp = [inf]*(len(T)+1)
dp[0] = 0

for _ in range(N):
    A, *S = input().split()
    # print(S)
    n_dp = dp[:]
    for s in S:
        for i in range(len(T)):
            if len(T) - i >= len(s):
                # print(T[i:i+len(s)], s)
                if T[i:i+len(s)] == s:
                    n_dp[i+len(s)] = min(n_dp[i+len(s)], dp[i]+1)
    dp = n_dp
    # print(dp)

if dp[-1] == inf:
    dp[-1] = -1

print(dp[-1])