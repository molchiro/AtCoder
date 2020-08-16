X, K, D = list(map(int, input().split()))

if abs(X) > K*D:
    print(abs(X) - K*D)
else:
    X = abs(X)
    K -= X//D
    X = X%D
    if K%2 == 0:
        print(X)
    else:
        print(abs(X-D))