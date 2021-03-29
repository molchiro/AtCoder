N = int(input())
d = dict()
keys = set()
d[0] = [0, 0]
keys.add(0)
for _ in range(N):
    X, C = list(map(int, input().split()))
    if C in keys:
        d[C][0] = min(d[C][0], X)
        d[C][1] = max(d[C][1], X)
    else:
        d[C] = [X, X]
        keys.add(C)
# print(d)
keys = list(keys)
keys.sort()
# dp[i][j]
# i番目のkeyにいてj=0の時、右=>左端に移動し、j=1の時はその逆の状態
dp = [[float('inf')]*2 for _ in range(len(keys))]
dp[0][0] = 0
dp[0][1] = 0
for i in range(len(keys)-1):
    curr_C = keys[i]
    next_C = keys[i+1]
    next_dist = d[next_C][1]-d[next_C][0]
    # l=>l
    dp[i+1][0] = min(dp[i+1][0], dp[i][0] + abs(d[curr_C][0]-d[next_C][1]) + next_dist)
    # r=>l
    dp[i+1][0] = min(dp[i+1][0], dp[i][1] + abs(d[curr_C][1]-d[next_C][1]) + next_dist)
    # l=>r
    dp[i+1][1] = min(dp[i+1][1], dp[i][0] + abs(d[curr_C][0]-d[next_C][0]) + next_dist)
    # r=>r
    dp[i+1][1] = min(dp[i+1][1], dp[i][1] + abs(d[curr_C][1]-d[next_C][0]) + next_dist)
    # print(keys[i+1], dp[i+1])
    # input()
ans = min(dp[-1][0] + abs(d[keys[-1]][0]), dp[-1][1] + abs(d[keys[-1]][1]))
print(ans)