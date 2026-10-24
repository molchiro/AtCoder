H, W, K = list(map(int, input().split()))

field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
row = [1]*H
col = [1]*W
ans = 0

for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == '#':
            row[h] = 0
            col[w] = 0
            field[h+1][w+1] = -1

stack = []
for h in range(H):
    for w in range(W):
        if row[h] and col[w]:
            stack.append((h+1, w+1))
            field[h+1][w+1] = 1
            ans += 1

for _ in range(K):
    tmp = []
    for h, w in stack:
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh, nw = h+dh, w+dw
            if field[nh][nw] == 0:
                field[nh][nw] = 1
                tmp.append((nh, nw))
                ans += 1
    stack = tmp

print(ans)