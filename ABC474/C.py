N, Q = list(map(int, input().split()))
P = list(map(int, input().split()))
address = [None]*(N+1)
for i, p in enumerate(P):
    address[p] = i

for _ in range(Q):
    a = int(input())
    idx = address[a]
    P.append(a)
    P[idx] = None
    address[a] = len(P)-1

ans = []
for p in P:
    if p == None:
        continue
    ans.append(p)

print(*ans)