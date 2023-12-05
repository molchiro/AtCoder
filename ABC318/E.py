N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

dd = defaultdict(list)

for i in range(N):
    dd[A[i]].append(i)

ans = 0

for idxs in dd.values():
    n = len(idxs)
    accum = 0
    for i in range(n-1):
        left = idxs[i]
        right = idxs[i+1]
        accum -= i
        accum += n-1-i
        ans += (right-left-1)*accum


print(ans)