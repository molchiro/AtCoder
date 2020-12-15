H, W = list(map(int, input().split()))
field = [[0]*W for _ in range(H)]
L = 0
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == '#':
            field[h][w] = 1
            L += 1

seen = [[0]*W for _ in range(H)]
ans = []

def solve(h, w, l):
    if not(0 <= h < H and 0 <= w < W):
        return

    if field[h][w] == 0:
        return
    
    if seen[h][w]:
        return
    
    # print(h, w, l)
    l += 1
    seen[h][w] = 1
    ans.append((h+1, w+1))
    if l >= L:
        print(L)
        for x, y in ans:
            print(x, y)
        exit()

    for dh, dw in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        solve(h+dh, w+dw, l)
    
    l -= 1
    seen[h][w] = 0
    ans.pop()

for i in range(H):
    for j in range(W):
        solve(i, j, 0)
