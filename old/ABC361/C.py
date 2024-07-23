N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
ans = float('inf')
for i in range(K+1):
    # print(i)
    ans = min(ans, A[i+N-K-1] - A[i])
print(ans)