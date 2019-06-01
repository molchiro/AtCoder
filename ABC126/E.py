N, M = list(map(int, input().split()))

L = [[1+i] for i in range(N)]

for i in range(M):
    X, Y, Z = list(map(int, input().split()))
    for i, el in enumerate(L):
        if X in el:
            X_i = i
            break
    X_L = L.pop(X_i)
    Y_i = -1
    for i, el in enumerate(L):
        if Y in el:
            Y_i = i
            break
    if Y_i != -1:
        Y_L = L.pop(Y_i)
        X_L.extend(Y_L)
    L.append(X_L)
print(len(L))