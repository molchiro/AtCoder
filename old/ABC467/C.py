N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [(A[i+1]+A[i])%M for i in range(N-1)]

ans = 10**18
for i in range(M):
    C_ = C[:]
    tmp = i
    C_[0] += i
    C_[0] %= M
    prev = 0
    for b, c in zip(B, C_):
        x = (b-(c+prev))%M
        tmp += x
        prev = x
    ans = min(ans, tmp)

print(ans)