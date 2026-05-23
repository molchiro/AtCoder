from collections import defaultdict

N, K = list(map(int, input().split()))
S = input()
dd = defaultdict(int)
for i in range(N-K+1):
    t = S[i:i+K]
    ct = 0
    for j in range(N-K+1):
        if S[j:j+K] == t:
            ct += 1
    dd[t] = max(dd[t], ct)

# print(dd)

M = max(dd.values())
ans = []
for k, v in dd.items():
    if v == M:
        ans.append(k)
ans.sort()

print(M)
print(*ans)