N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))

from collections import deque

dq = deque()
accum = 0

for a in A:
    if accum + a > K:
        print('No')
        dq.append(0)
    else:
        print('Yes')
        dq.append(a)
        accum += a

    if len(dq) >= M:
        accum -= dq.popleft()