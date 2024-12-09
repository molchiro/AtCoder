from atcoder.modint import Modint, ModContext
from collections import defaultdict, Counter


mod = 998244353
with ModContext(mod):

    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    cumsum = [0]
    for a in A:
        cumsum.append(cumsum[-1]+a)

    counter = Counter(cumsum[2:])
    S = set(cumsum[2:])

    # print(counter)

    dp = defaultdict(Modint)
    dp[A[0]] += 1
    INF = 10**18

    for i in range(1, N):
        a = A[i]

        c = cumsum[i+1]

        ndp = defaultdict(Modint)

        for k, v in dp.items():

            # 閉じる
            if k != K:
                ndp[a] += v

            # 足す
            x = k+a
            if K - x+c in S:
                ndp[x] += v
            else:
                ndp[INF] += v

        dp = ndp

        counter[c] -= 1
        if counter[c] == 0:
            S.remove(c)

    ans = Modint(0)
    for k, v in dp.items():
        if k != K:
            ans += v
    print(ans.val())