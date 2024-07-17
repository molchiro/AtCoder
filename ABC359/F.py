N = int(input())
A = list(map(int, input().split()))
ans = sum(A)

from heapq import heapify, heappop, heappush

d = {}
for i in range(1, 2*(10**5)+1):
    d[i] = (i+1)**2 - (i**2)

hq = []
for a in A:
    heappush(hq, (a*d[1], a, 1))

for _ in range(N-2):
    delta, a, k = heappop(hq)
    ans += delta
    heappush(hq, (a*d[k+1], a, k+1))

print(ans)