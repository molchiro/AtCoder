A = list(map(int, input().split()))

from collections import Counter

c = Counter(A)

if len(c) == 1:
    print(2)
else:
    ans = 0
    for v in c.values():
        if v >= 2:
            ans += 1
    print(ans)