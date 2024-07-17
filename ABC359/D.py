from atcoder.modint import Modint, ModContext
from collections import defaultdict

mod = 998244353
with ModContext(mod):
    N, K = list(map(int, input().split()))
    S = input()

    dp = defaultdict(Modint)
    dp['X'*K] = Modint(1)

    for s in S:
        ndp = defaultdict(Modint)

        for x in dp.keys():
            for ns in ['A', 'B'] if s == '?' else [s]:
                nx = x[1:] + ns
                if nx != nx[::-1]:
                    ndp[nx] += dp[x]

        dp = ndp

    ans = Modint()
    for x in dp.values():
        ans += x
    print(ans.val())