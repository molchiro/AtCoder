from collections import defaultdict

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

dd = defaultdict(int)
for a in A:
    dd[a] += 1

ans = 0
i = 0
while K > 0:
    if dd[i] < K:
        ans += i*(K-dd[i])
        K = dd[i]
    i += 1

print(ans)