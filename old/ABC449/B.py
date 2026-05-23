H, W, Q = list(map(int, input().split()))
for _ in range(Q):
    t, v = list(map(int, input().split()))
    if t == 1:
        print(W*v)
        H -= v
    else:
        print(H*v)
        W -= v