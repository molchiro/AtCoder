N, K = list(map(int, input().split()))

from collections import deque

dq = deque([1 for _ in range(K)])

accum = K
for _ in range(N-K+1):
    dq.append(accum)
    accum += accum
    accum %= 10**9
    accum -= dq.popleft()
    accum %= 10**9

print(dq[-1])