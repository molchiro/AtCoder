import heapq

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)
if sum(A) <= K:
    print(0)
else:
    X = [(-A[i]*F[i], A[i], F[i]) for i in range(N)]
    heapq.heapify(X)
    x = heapq.heappop(X)
    for i in range(K-1):
        x = heapq.heappushpop(X, (-(x[1]-1)*x[2], x[1]-1, x[2]))
    heapq.heappush(X, (-(x[1]-1)*x[2], x[1]-1, x[2]))
    print(max(map(lambda x: -x[0], X)))