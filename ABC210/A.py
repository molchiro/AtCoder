N, A, X, Y = list(map(int, input().split()))

B = max(0, N-A)
print(X*min(N, A)+Y*B)