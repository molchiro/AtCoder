N = input()
UL = 9*14
# ある数aをmodに取ると固定した時の桁DPを全パターン計算する
ans = 0
for a in range(1, UL+1):
    # dp[k][r][f] k: 桁和 r: 余り f:　未満フラグ
    dp = [[[0]*2 for _ in range(UL+1)] for _ in range(UL+1)]
    dp[0][0][0] = 1
    for s in N:
        dp_nxt = [[[0]*2 for _ in range(UL+1)] for _ in range(UL+1)]
        for k in range(a+1):
            for r in range(a+1):
                for d in range(10):
                    k_nxt = k+d
                    r_nxt = (r*10+d)%a
                    if k_nxt > UL:
                        continue
                    # less -> less
                    dp_nxt[k_nxt][r_nxt][1] += dp[k][r][1]
                    # eq -> less
                    if d < int(s):
                        dp_nxt[k_nxt][r_nxt][1] += dp[k][r][0]
                    # eq -> eq
                    if d == int(s):
                        dp_nxt[k_nxt][r_nxt][0] += dp[k][r][0]
        dp = dp_nxt
    ans += dp[a][0][0] + dp[a][0][1]
print(ans)