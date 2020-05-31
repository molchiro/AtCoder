import bisect

N = int(input())
A = [-int(input()) for i in range(N)]
X = []
for i in range(N):
    a = A[i]
    idx = bisect.bisect(X, a)
    if idx == len(X):
        X.append(a)
    else:
        X[idx] = a
print(len(X))