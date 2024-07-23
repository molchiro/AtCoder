from math import ceil
A, M, L, R = list(map(int, input().split()))
A %= M
if L < 0:
    tmp = abs(L)//M + 1
    # print(tmp)
    L += tmp*M
    R += tmp*M
# print(A, M, L, R)
ans = R//M + (1 if A <= R%M else 0) - (L-1)//M - (1 if A <= (L-1)%M else 0) 
print(ans)

