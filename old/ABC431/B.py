X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

f = [0]*N
for _ in range(Q):
    P = int(input())-1
    if f[P] == 0:
        X += W[P]
        f[P] = 1
    else:
        X -= W[P]
        f[P] = 0
    print(X)
        