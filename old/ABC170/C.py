X, N = list(map(int, input().split()))
P = set(list(map(int, input().split())))
for i in range(100):
    if not (X-i) in P:
        print(X-i)
        break
    if not (X+i) in P:
        print(X+i)
        break