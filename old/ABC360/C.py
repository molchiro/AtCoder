N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
ans = sum(W)
from collections import defaultdict
dd = defaultdict(list)
for a, w in zip(A, W):
    dd[a].append(w)

for v in dd.values():
    ans -= max(v)

print(ans)