import bisect

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)
if sum(A) <= K:
    print(0)
else:
    left = 0
    right = max([A[i]*F[i] for i in range(N)])
    while left + 1 != right:
        mid = int((left + right + 1) / 2)
        train_n = sum([A[i]-mid//F[i] for i in range(N)])
        if train_n > K:
            left = mid
        else:
            right = mid
    print(right)
