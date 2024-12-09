N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

from collections import defaultdict

dd = defaultdict(int)
accum = 0

for i in range(N-1):
    accum += A[i]
    accum %= M
    dd[accum] += 1

ans = 0
now = 0
for i in range(N):
    # print(now, accum, dd)
    ans += dd[(M-(-now%M))%M]
    now += A[i]
    now %= M
    dd[now] -= 1
    accum += A[i-1]
    accum %= M
    dd[accum] += 1
    # print(ans)

print(ans)
