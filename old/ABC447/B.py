S = input()

from collections import Counter

counter = Counter(S)
M = max(counter.values())

ans = ''
for s in S:
    if counter[s] != M:
        ans += s
print(ans)