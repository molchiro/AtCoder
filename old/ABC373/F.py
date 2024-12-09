from collections import defaultdict
from heapq import heapify, heappop, heappush

N, W = list(map(int, input().split()))
dd = defaultdict(list)
for _ in range(N):
    w, v = list(map(int, input().split()))
    dd[w].append(v)

# print(dd[3])

dp = [-1]*(W+1)
dp[0] = 0
for w in range(1, W+1):
    if len(dd[w]) == 0:
        continue
    
    hq = []
    for v in dd[w]:
        heappush(hq, (-(v-1)))

    
    for i in range(1, W//w+1):
        # print(hq)
        d = heappop(hq)
        d *= -1
        heappush(hq, -(d-2))
        if d < 0:
            continue

        # print(w, i, d)
        for j in range(W, w-1, -1):
            # print(j, w, i)
            if dp[j-w] == -1:
                continue

            else:
                dp[j] = max(dp[j], dp[j-w]+d)
        # print(dp)

# print(dp)
print(max(dp))

