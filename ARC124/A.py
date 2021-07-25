N, K = list(map(int, input().split()))
A = [[1]*K for _ in range(N)]
for i in range(K):
    c, k = input().split()
    k = int(k)-1
    if c =='L':
        for j in range(k):
            A[j][i] = 0
        A[k] = [0]*K
        A[k][i] = 1
    else:
        for j in range(k+1, N):
            A[j][i] = 0
        A[k] = [0]*K
        A[k][i] = 1
# print(A)
ans = 1
for i in range(N):
    ans *= sum(A[i])
    ans %= 998244353
print(ans)