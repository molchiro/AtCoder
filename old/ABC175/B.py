from collections import Counter
from itertools import combinations

N = int(input())
L = Counter(list(map(int, input().split())))
ans = 0
for sides in combinations(L.keys(), 3):
    a, b, c = sorted(sides)
    if a + b > c:
        ans += L[a]*L[b]*L[c]
print(ans)