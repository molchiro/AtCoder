from sortedcontainers import SortedSet

N, K = list(map(int, input().split()))
P = list(map(int, input().split()))
P_i = []
for i, p in enumerate(P):
    P_i.append((p, i))
P_i.sort()
sd = SortedSet([])
for i in range(K):
    sd.add(P_i[i][1])

ans = sd[-1]-sd[0]
for i in range(K, N):
    sd.add(P_i[i][1])
    sd.remove(P_i[i-K][1])
    ans = min(ans, sd[-1]-sd[0])
print(ans)