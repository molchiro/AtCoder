import math

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
S = list(map(int, input().split()))
for s in S:
    X = s
    for i in range(N):
        X = math.gcd(X, A[i])
        if X == 1:
            print(i+1)
            break
    else:
        print(X)