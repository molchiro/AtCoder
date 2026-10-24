from heapq import heapify, heappop, heappush

hq = []

Q = int(input())

for _ in range(Q):
    t, h = list(map(int, input().split()))
    if t == 1:
        heappush(hq, h)
    else:
        while hq and hq[0] <= h:
            heappop(hq)

    print(len(hq))