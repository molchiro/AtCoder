N, M, L  = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [0]
for i in range(L):
    B.append(B[-1]+A[i])
for i in range(L, N):
    B.append(B[-1]-A[i-L]+A[i])
B = B[L:]
B = [(M-b)%M for b in B]
# print(B)

ans = 10**18
for i in range(N-L+1):
    C = B[:]
    # 左から
    for j in range(1,i+1):
        if C[j] < C[j-1]:
            a = C[j-1]-C[j]
            C[j] += M
    # 右から
    for j in range(N-L-1, i-1, -1):
        if C[j] < C[j+1]:
            a = C[j+1]-C[j]
            C[j] += M
    # print(C)
    ans = min(ans, max(C))
print(ans)
