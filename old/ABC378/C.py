N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

dd = defaultdict(lambda: -1)

ans = []
for i, a in enumerate(A):
    ans.append(dd[a])
    dd[a] =i+1
print(*ans)