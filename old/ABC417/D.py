N = int(input())
items = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i番目のプレゼントをもらう直前でのテンションがjの時に最終的にテンションがいくつになるか
dp = [[0]*1001 for _ in range(N)]

P, A, B = items[-1]
for j in range(1001):
    if P >= j:
        dp[-1][j] = j+A
    else:
        dp[-1][j] = max(j-B, 0)

for i in range(N-2, -1, -1):
    P, A, B = items[i]
    for j in range(1001):
        if P >= j:
            dp[i][j] = dp[i+1][j+A]
        else:
            dp[i][j] = dp[i+1][max(j-B, 0)]

cumsum = [0]
for P, A, B in items:
    cumsum.append(cumsum[-1] + B)
# print(cumsum)

from bisect import bisect_left, bisect_right

Q = int(input())
for _ in range(Q):
    X = int(input())
    if X <= 1000:
        print(dp[0][X])
    else:
        # X -= 1000
        idx = bisect_left(cumsum, X - 1000)
        # print(X, idx)
        if idx >= N:
            print(X - cumsum[-1])
        else:
            X -= cumsum[idx]
            # print('yyyy')
            print(dp[idx][X])
