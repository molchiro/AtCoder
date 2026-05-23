N, Q = list(map(int, input().split()))

from heapq import heapify, heappop, heappush
from collections import defaultdict

hq = []
dd = defaultdict(int)
for i in range(1, N+1):
    heappush(hq, i)
    dd[i] += 1

for _ in range(Q):
    X, Y = list(map(int, input().split()))
    ans = 0
    while hq[0] <= X:
        x = heappop(hq)
        ans += dd[x]
        dd[x] = 0
    dd[Y] += ans
    heappush(hq, Y)
    print(ans)