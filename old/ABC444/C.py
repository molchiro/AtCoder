N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = []

# 一番長かったものが折れたものではない場合
M = A[-1]
B = A[:]
C = []

while B and B[-1] == M:
    C.append(B.pop())
# print(B)
# print(C)
if len(B)%2 == 0:
    f = 1
    for i in range(len(B)//2):
        if B[i]+B[-1-i] != M:
            f = 0
    if f:
        ans.append(M)

# 全て折れていた場合
if N%2 == 0:
    L = A[0]+A[-1]
    f = 1
    for i in range(N//2):
            if A[i]+A[-1-i] != L:
                f = 0
    if f:
        ans.append(L)

print(*ans)