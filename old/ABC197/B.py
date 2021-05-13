H, W, Y, X = list(map(int, input().split()))
S = [input() for _ in range(H)]
ans = 0
x = X-1
while x >= 0:
    if S[Y-1][x] == '#':
        break
    ans += 1
    x -= 1
x = X-1
while x < W:
    if S[Y-1][x] == '#':
        break
    ans += 1
    x += 1
y = Y-1
while y >= 0:
    if S[y][X-1] == '#':
        break
    ans += 1
    y -= 1
y = Y-1
while y < H:
    if S[y][X-1] == '#':
        break
    ans += 1
    y += 1
print(ans - 3)