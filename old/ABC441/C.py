N, K, X = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)
now = 0
ct = 0
for i in range(N-K, N):
    now += A[i]
    if now >= X:
        print(i+1)
        break
else:
    print(-1)