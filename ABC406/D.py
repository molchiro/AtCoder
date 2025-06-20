H, W, N = list(map(int, input().split()))
r_ct = [0]*H
c_ct = [0]*W

r_table = [[] for _ in range(H)]
c_table = [[] for _ in range(W)]

for _ in range(N):
    X, Y = list(map(lambda x: int(x) - 1, input().split()))
    r_ct[X] += 1
    c_ct[Y] += 1
    r_table[X].append(Y)
    c_table[Y].append(X)

removed = set()
Q = int(input())
for _ in range(Q):
    t, v = list(map(lambda x: int(x) - 1, input().split()))
    if t == 0:
        print(r_ct[v])
        r_ct[v] = 0
        for c in r_table[v]:
            if (v, c) in removed:
                continue
            c_ct[c] -= 1
            removed.add((v, c))
        r_table[v] = []
    else:
        print(c_ct[v])
        c_ct[v] = 0
        for r in c_table[v]:
            if (r, v) in removed:
                continue
            r_ct[r] -= 1
            removed.add((r, v))
        c_table[v] = []
    