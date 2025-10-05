from collections import defaultdict
mod = 998244353

N = int(input())
T = input()

patterns = set([T])
dp = defaultdict(int)
dp[T] += 1
while patterns:
    np = set()
    ndp = defaultdict(int)
    for pattern in patterns:
        seen = set()
        # print(pattern)
        for i in range(len(pattern)):
            s = pattern[:i] + pattern[i+1:]
            if s in seen:
                continue
            ndp[s] += dp[pattern]
            ndp[s] %= mod
            seen.add(s)
            np.add(s)
    patterns = np
    dp = ndp
    # print(dp)
    # input()
    if "" in dp:
        break

print(dp[""])            