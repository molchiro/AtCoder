X, Y, Z, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

AB = []
for i in range(min(X,K)):
    for j in range(min(Y,K)):
        AB.append(A[i] + B[j])

AB.sort(reverse=True)

ABC = []
for i in range(min(X*Y,K)):
    for j in range(min(Z,K)):
        ABC.append(AB[i] + C[j])

ABC.sort(reverse=True)

for i in range(K):
    print(ABC[i])


