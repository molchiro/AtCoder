N, M, C = list(map(int, input().split()))
A = list(map(int, input().split()))
from collections import Counter
CT = Counter(A)
B = list(CT.items())
B.sort()
# print(B)

from collections import deque

dq1 = deque(B)
for k, v in B:
    dq1.append((k+M, v))
dq1.append((10**18, 10**18))
# print(dq1)

accum = 0
dq2 = deque()
while accum < C:
    k, v = dq1.popleft()
    accum += v
    dq2.append((k, v))

D = []
prev = 0
for k, _ in B:
    D.append((k, k-prev))
    prev = k
D.append((M, M-prev))
# print(D)

ans = 0
for i, n in D:
    ans += accum*n
    # print(i, n, accum)
    # 左端を捨てる
    while dq2 and dq2[0][0] <= i:
        k, v = dq2.popleft()
        accum -= v
    
    # 右端をとる
    while accum < C:
        k, v = dq1.popleft()
        accum += v
        dq2.append((k, v))

print(ans)