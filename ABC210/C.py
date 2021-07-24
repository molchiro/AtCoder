from collections import defaultdict

N, K = list(map(int, input().split()))
C = list(map(int, input().split()))

d = {}
keys = set()
kinds_in_K = 0
for i in range(K):
    c = C[i]
    if c in keys:
        d[c] += 1
    else:
        kinds_in_K += 1
        d[c] = 1
        keys.add(c)

ans = kinds_in_K
for i in range(K, N):
    c_push = C[i]
    c_pop = C[i-K]
    if c_push in keys:
        d[c_push] += 1
    else:
        kinds_in_K += 1
        d[c_push] = 1
        keys.add(c_push)
    if d[c_pop] == 1:
        kinds_in_K -= 1
        d[c_pop] = 0
        keys.remove(c_pop)
    else:
        d[c_pop] -= 1
    ans = max(ans, kinds_in_K)

print(ans)