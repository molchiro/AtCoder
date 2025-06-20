N, M = list(map(int, input().split()))
P = list(map(int, input().split()))

from heapq import heapify, heappop, heappush

hq = [(p, (i, 1)) for i, p in enumerate(P)]
heapify(hq)

ans = 0
while M:
    p, (i, n) = heappop(hq)
    if p > M:
        break
    
    ans += 1
    M -= p
    print(M, p, i, n)
    heappush(hq, (P[i]*(2*(n)+1), (i, n+1)))

print(ans)