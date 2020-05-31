import heapq
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = [-x for x in Counter(A).values()]
heapq.heapify(B)
for i in range(1, N+1):
    B_ = B[:]
    cnt = 0
    while len(B_) >= i:
        cnt += 1
        tmp = []
        for j in range(i):
            x = heapq.heappop(B_)
            if x < -1:
                tmp.append(x + 1)
        for b in tmp:
            heapq.heappush(B_, b)
    print(cnt)
