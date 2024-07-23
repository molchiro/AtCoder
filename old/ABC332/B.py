K, G, M = list(map(int, input().split()))
g = 0
m = 0
for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        if m > G-g:
            m -= G-g
            g = G
        else:
            g += m
            m = 0

print(g, m)