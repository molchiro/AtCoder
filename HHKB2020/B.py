H, W = list(map(int, input().split()))
S = [input()+'#' for _ in range(H)]
S.append('#'*(W+1))
ans = 0
for i in range(H):
    for j in range(W):
        x = S[i][j]
        y = S[i+1][j]
        z = S[i][j+1]
        if x == '.' and y == '.':
            ans += 1
        if x == '.' and z == '.':
            ans += 1
print(ans)