import bisect

N = int(input())
A = [-int(input()) for i in range(N)]
X = []
for i in range(N):
    a = A[i]
    idx = bisect.bisect_left(X, a+0.1)
    if idx == len(X):
        X.append(a)
    else:
        X[idx] = a
print(len(X))