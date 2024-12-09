from collections import defaultdict
from itertools import accumulate

S = input()

dd = defaultdict(list)

for i, s in enumerate(S):
    dd[s].append(i)

ans = 0
for k, v in dd.items():
    l = len(v)
    if l < 2:
        continue

    cumsum = list(accumulate(v, initial=0))
    for i in range(l-1):
        ans += (cumsum[-1]-cumsum[i+1]) - (v[i]+1)*(l-1-i)

print(ans)
