from heapq import heapify, heappop, heappush

T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = list(zip(A, B))
    AB.sort()

    # print(AB)

    accum = 0
    hq = []
    for i in range(K):
        a, b = AB[i]
        accum += b
        heappush(hq, -b)

    # print(accum, hq)
    
    ans = AB[K-1][0]*accum
    # print(ans)
    for i in range(K, N):
        a, b = AB[i]
        accum -= -heappop(hq)
        accum += b
        ans = min(ans, a*accum)
        heappush(hq, -b)
        # print(accum, hq)
    print(ans)