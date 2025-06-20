H, W = list(map(int, input().split()))
field = [input() for _ in range(H)]

l = 10**18
r = 0
t = 10**18
b = 0 
for h in range(H):
    for w in range(W):
        if field[h][w] == '#':
            l = min(l, w)
            r = max(r, w)
            t = min(t, h)
            b = max(b, h)

# startとendの内側が#か?で、startとendの外側に#があってはならない
f = 1
for h in range(H):
    for w in range(W):
        if t <= h <= b and l <= w <= r:
            if not field[h][w] in ['#', '?']:
                f = 0
        else:
            if field[h][w] == '#':
                f = 0

print('Yes' if f else 'No')