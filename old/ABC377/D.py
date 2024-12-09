from collections import defaultdict
from heapq import heapify, heappop, heappush

N, M = list(map(int, input().split()))
d = defaultdict(list)
for _ in range(N):
    L, R = list(map(int, input().split()))
    d[R].append(L)

hq = [0]
ans = 0
for r in range(1, M+1):
    for L in d[r]:
        heappush(hq, -L)
    
    l = - hq[0]

    ans += r-l
    # print(r, hq)

print(ans)