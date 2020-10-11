H, W = list(map(int, input().split()))
S = [input()+'#' for _ in range(H)]
S.append('#'*(W+1))

dots = 0
for s in S:
    dots += s.count('.')

renzoku = [[-1]*W for _ in range(H)]
for w in range(W):
    s = 0
    for h in range(H+1):
        if S[h][w] == '.':
            continue
        else:
            for i in range(s, h):
                renzoku[i][w] += h-s
            s = h + 1
for h in range(H):
    s = 0
    for w in range(W+1):
        if S[h][w] == '.':
            continue
        else:
            for i in range(s, w):
                renzoku[h][i] += w-s 
            s = w + 1

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        ans += (2**renzoku[i][j] - 1)*(2**(dots-renzoku[i][j]))
        ans %= 1000000007
print(ans)