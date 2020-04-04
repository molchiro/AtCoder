# import bisect

# N, M = list(map(int, input().split()))
# A = list(map(lambda x: int(x) * -1, input().split()))
# A.sort()

# cnt = 1
# while cnt <= M:
#     x = bisect.bisect(A, A[0]/2)
#     for i in range(x):
#         A[i] /= 2
#         cnt += 1
#         if cnt > M:
#             break
#     if x != 0 or x != len(A):
#         A.sort()
# print(sum(map(lambda x: int(-x), A)))

import heapq

N, M = list(map(int, input().split()))
A = list(map(lambda x: int(x) * -1, input().split()))
heapq.heapify(A)

for i in range(M):
    heapq.heappush(A, heapq.heappop(A)/2)
print(sum(map(lambda x: int(-x), A)))