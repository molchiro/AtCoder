T = int(input())
for _ in range(T):
    now = 0
    N, H = list(map(int, input().split()))
    hl = H
    hu = H
    f = 1
    for _ in range(N):
        t, l, u = list(map(int, input().split()))
        dt = t - now
        now = t
        hl -= dt
        hl = max(1, hl)
        hu += dt
        if u < hl or l > hu:
            f = 0
        hu = min(hu, u)
        hl = max(l, hl)
    print('Yes' if f else 'No')