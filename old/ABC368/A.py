N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A = A[N-K:] + A[:N-K]
print(*A)