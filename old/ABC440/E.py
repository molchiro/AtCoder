N, K, X = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)

from heapq import heapify, heappop, heappush

hq = [(-A[0]*K, tuple([K] + [0]*(N-1)))]
seen = set(tuple([K] + [0]*(N-1)))
for _ in range(X):
    v, k = heappop(hq)
    print(-v)
    for i in range(N-1):
        if k[i] == 0:
            continue

        new_k = list(k)
        new_k[i] -= 1
        new_k[i+1] += 1
        new_k = tuple(new_k)
        if new_k in seen:
            continue

        seen.add(new_k)
        heappush(hq, (v + A[i] - A[i+1], new_k))