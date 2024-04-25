N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(10**6+1):
# for i in range(20):
    Q_ = [Q[j]-A[j]*i for j in range(N)]
    if not all([q >= 0 for q in Q_]):
        break
    j = 10**6+1
    for k in range(N):
        if B[k] > 0:
            j = min(j, Q_[k]//B[k])
    ans = max(ans, i+j)
    # print(ans, Q_)
print(ans)