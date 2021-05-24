H, W = list(map(int, input().split()))
field = [input() for _ in range(H)]
ans = 1
for i in range(H+W-1):
    elements = set()
    for h in range(H):
        w = i-h
        if 0 <= w < W:
            elements.add(field[h][w])
    # print(i, elements)
    if elements == {'.'}:
        ans *= 2
    elif 'B' in elements and 'R' in elements:
        ans *= 0
    ans %= 998244353
print(ans)