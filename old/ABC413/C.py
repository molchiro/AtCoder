Q = int(input())
from collections import deque
dq = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, c, x = query
        dq.append((x, c))
    else:
        _, k = query
        ans = 0
        while k > 0:
            x, c = dq.popleft()
            if c <= k:
                ans += x*c
                k -= c
            else:
                ans += x*k
                dq.appendleft((x, c-k))
                k = 0
        print(ans)
    # print(dq)