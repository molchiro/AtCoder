# 前と後ろのABCは消してから始める
# XXXABCXXXのとき、2つ増やすのは6手  XXABCXXXXなら9手かかる
# dpっぽい
# dp[i][j][k] i番目までみた, jこABCがある, 直前が['','A','AB']の状態のいずれかk番目 である時の操作回数の最小値

T = int(input())
for _ in range(T):
    S = input()

    S_ = list(S)
    while len(S_) >= 3 and S_[-3] == 'A' and S_[-2] == 'B' and S_[-1] == 'C':
        S_.pop()
        S_.pop()
        S_.pop()
    S_.reverse()
    while len(S_) >= 3 and S_[-3] == 'C' and S_[-2] == 'B' and S_[-1] == 'A':
        S_.pop()
        S_.pop()
        S_.pop()
    S_.reverse()
    S = ''.join(S_)
    # print(S)

    K = int(input())
    n = S.count('ABC')
    dp = [[10**18]*(3) for _ in range(n+K+2)]
    dp[0][0] = 0
    for s in S:
        ndp = [[10**18]*(3) for _ in range(n+K+2)]
        for j in range(n+K+1):

            if s == 'A':
                # 書き換えない
                ndp[j][1] = min(ndp[j][1], min(dp[j]))
                # Bに書き換える
                ndp[j][0] = min(ndp[j][0], min(dp[j][0], dp[j][2])+1)
                ndp[j][2] = min(ndp[j][2], dp[j][1]+1)
                # Cに書き換える
                ndp[j][0] = min(ndp[j][0], min(dp[j][0], dp[j][1])+1)
                ndp[j+1][0] = min(ndp[j+1][0], dp[j][2]+1)
            elif s == 'B':
                # 書き換えない
                ndp[j][0] = min(ndp[j][0], min(dp[j][0], dp[j][2]))
                ndp[j][2] = min(ndp[j][2], dp[j][1])
                # Aに書き換える
                ndp[j][1] = min(ndp[j][1], min(dp[j])+1)
                # Cに書き換える
                ndp[j][0] = min(ndp[j][0], min(dp[j][0], dp[j][1])+1)
                ndp[j+1][0] = min(ndp[j+1][0], dp[j][2]+1)
            elif s == 'C':
                # 書き換えない
                ndp[j][0] = min(ndp[j][0], min(dp[j][0], dp[j][1]))
                ndp[j+1][0] = min(ndp[j+1][0], dp[j][2])
                # Aに書き換える
                ndp[j][1] = min(ndp[j][1], min(dp[j])+1)
                # Bに書き換える
                ndp[j][0] = min(ndp[j][0], min(dp[j][0], dp[j][2])+1)
                ndp[j][2] = min(ndp[j][2], dp[j][1]+1)
            else:
                # 書き換えない
                ndp[j][0] = min(ndp[j][0], min(dp[j]))
                # Aに書き換える
                ndp[j][1] = min(ndp[j][1], min(dp[j])+1)
                # Bに書き換える
                ndp[j][0] = min(ndp[j][0], min(dp[j][0], dp[j][2])+1)
                ndp[j][2] = min(ndp[j][2], dp[j][1]+1)
                # Cに書き換える
                ndp[j][0] = min(ndp[j][0], min(dp[j][0], dp[j][1])+1)
                ndp[j+1][0] = min(ndp[j+1][0], dp[j][2]+1)


        dp = ndp
    ans = min(dp[n+K])
    if ans == 10**18:
        ans = -1
    print(ans)