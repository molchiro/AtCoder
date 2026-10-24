mod = 998244353

S = input()

# dp[i][c] i番目まで見て最後の文字がcであるような選び方の集合(カラ文字を27番目の文字とする)

dp = [0]*27
dp[-1] = 1

for s in S:
    idx = ord(s) - ord('a')
    ndp = dp[:]
    for c in range(27):
        if c == idx:
            continue
        ndp[idx] += dp[c]
    ndp[idx] %= mod
    dp = ndp

print(sum(dp[:26])%mod)
