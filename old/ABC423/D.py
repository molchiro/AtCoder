from heapq import heapify, heappop, heappush
from collections import deque

N, K = list(map(int, input().split()))
groups = [list(map(int, input().split())) for _ in range(N)]

hq =[(a, (0, i, b, c)) for i, (a, b, c) in enumerate(groups)]
heapify(hq)

ans = [10**18]*N

dq = deque()
n = 0
while hq:
    # イベント管理
    a, (t, *args) = heappop(hq)
    if t == 0:
        i, b, c = args
        dq.append((i, b, c))
    else:
        c = args[0]
        n -= c

    # 待ち行列管理
    while dq and dq[0][2] + n <= K:
        i, b, c = dq.popleft()
        ans[i] = a
        heappush(hq, (a+b, (1, c)))
        n += c

print(*ans, sep='\n')

