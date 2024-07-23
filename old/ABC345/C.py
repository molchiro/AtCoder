S = input()
from collections import Counter
c = Counter(list(S))

n = len(S)
ans = 1 if len(set(list(S))) != len(S) else 0

for s in S:
    c[s] -= 1
    n -= 1
    ans += n - c[s]


print(ans)