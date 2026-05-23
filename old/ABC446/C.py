from collections import deque
T = int(input())
for _ in range(T):
    N, D = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    stock = deque()
    for i in range(N):
        for _ in range(A[i]):
            stock.append(i)
        for _ in range(B[i]):
            stock.popleft()
        while stock and (i - stock[0] >= D):
            stock.popleft()
    print(len(stock))
