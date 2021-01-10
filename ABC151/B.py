N, K, M = list(map(int, input().split()))
A = list(map(int, input().split()))
x = N*M - sum(A)
if x <= K:
    print(max(0, x))
else:
    print(-1)