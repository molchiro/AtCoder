H, W = list(map(int, input().split()))
N = int(input())
AB  = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
As = set([a for a, _ in AB])
d = {k: i for i, k in enumerate(sorted(list(As)))}
# print(d)

M = len(As)
doors = [[] for _ in range(M)]
for i in range(N):
    doors[d[AB[i][0]]].append(AB[i][1])
# print(doors)

# dp[i][status]: i番目まで見たときstatusの状態を満たすような移動方法の最小値
# status
#   0 -> 両方左
#   1 -> 両方右
#   2 -> 片方ずつ

dp = [0]*3
# dp[0] = 0
for i in range(M):
    row = doors[i]
    ndp = [10**18]*3

    # 0 -> 0
    ndp[0] = min(ndp[0], dp[0] + row[-1]*2)
    # 0 -> 1
    ndp[1] = min(ndp[1], dp[0] + 2*(W-1))
    # 0 -> 2
    ndp[2] = min(ndp[2], dp[0] + (W-1))

    # 1 -> 0
    ndp[0] = min(ndp[0], dp[1] + 2*(W-1))
    # 1 -> 1
    ndp[1] = min(ndp[1], dp[1] + (W-1-row[0])*2)
    # 1 -> 2
    ndp[2] = min(ndp[2], dp[1] + W-1)

    # 2 -> 0
    ndp[0] = min(ndp[0], dp[2] + W-1)
    # 2 -> 1
    ndp[1] = min(ndp[1], dp[2] + W-1)
    # 2 -> 2
    x = 10**18
    arr = [0] + row[:] + [W-1]
    for j in range(len(arr)-1):
        l = arr[j]
        r = arr[j+1]
        x = min(x, 2*l + 2*(W-1-r))
    ndp[2] = min(ndp[2], dp[2] + x)


    dp = ndp
    print(row, dp)

print(dp[0])