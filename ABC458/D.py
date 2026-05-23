X = int(input())
Q = int(input())

from heapq import heapify, heappop, heappush

hq1 = [0]
hq2 = [10**18]

for _ in range(Q):
    A, B = list(map(int, input().split()))
    l = - heappop(hq1)
    r = heappop(hq2)
    array = [A, B, l, r, X]
    array.sort()
    # print(array, hq1, hq2)
    X = array[2]
    heappush(hq1, -array[0])
    heappush(hq1, -array[1])
    heappush(hq2, array[3])
    heappush(hq2, array[4])

    print(X)