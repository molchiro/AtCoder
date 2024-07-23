N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
if K%2 == 0:
    ans = 0
    for i in range(0, K, 2):
        ans += A[i+1] - A[i]
    print(ans)
else:
    tmp = 0
    for i in range(0, K-1, 2):
        tmp += A[i+2] - A[i+1]
    ans = tmp
    for i in range(0, K-1, 2):
        tmp -= A[i+2] - A[i+1]
        tmp += A[i+1] - A[i]
        ans = min(ans, tmp)
    print(ans)
        