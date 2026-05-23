N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

for a in A:
    if a < X:
        X = a
        print(1)
    else:
        print(0)