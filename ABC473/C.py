N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
from collections import Counter
c = Counter(A)

kv = list(c.items())
kv.sort(key=lambda x: x[1])

top = kv[-1][1]

ans = 0
for i in range(1, N+1):
    if c[i]+1 < top:
        continue
    ans += 1
print(ans)