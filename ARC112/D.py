from collections import deque

H, W = list(map(int, input().split()))
field = [[0]*W for _ in range(H)]
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == '#':
            field[h][w] = 1
field[0][0] = 1
field[-1][0] = 1
field[0][-1] = 1
field[-1][-1] = 1

groups = []
for h in range(H):
    for w in range(W):
        dq = deque()
        seen_H = set()
        seen_W = set()
        if field[h][w]:
            dq.append((h, w))
            field[h][w] = 0
            seen_H.add(h)
            seen_W.add(w)
            while dq:
                s, t = dq.popleft()
                for i in range(H):
                    if field[i][w]:
                        dq.append((i, w))
                        field[i][w] = 0
                        seen_H.add(i)
                        seen_W.add(w)
                for i in range(W):
                    if field[h][i]:
                        dq.append((h, i))
                        field[h][i] = 0
                        seen_H.add(h)
                        seen_W.add(i)
                if len(seen_H) >= H:
                    print(0)
                    exit()
                if len(seen_W) >= W:
                    print(0)
                    exit()
            groups.append((len(seen_H), len(seen_W)))

row = [x[0] for x in groups]
col = [x[1] for x in groups]

# print(row)
# print(col)

ans = min(H-sum(row)+len(row)-1, W-sum(col)+len(col)-1)
print(ans)
