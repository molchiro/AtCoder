H, W = list(map(int, input().split()))
field_input = []
for _ in range(H):
    field_input.append(list(input()))

# 探索マップ　スタート地点からの距離を格納。初期値が無限、侵入禁止は-1
field_exp = [[-1]*(W+2)] + [[-1]+ [float('inf')]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
for h in range(H):
    for w in range(W):
        if field_input[h][w] == '.':
            continue
        elif field_input[h][w] == '#':
            field_exp[h+1][w+1] = -1
        elif field_input[h][w] == 'S':            
            start = (h, w)
        elif field_input[h][w] == 'G':
            goal = (h, w)
        else:
            direction_dic = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
            dh, dw = direction_dic[field_input[h][w]]
            field_exp[h+1][w+1] = -1
            i = 1
            while 0 <= h + dh*i < H and 0 <= w + dw*i < W:
                if field_input[h+dh*i][w+dw*i] != '.':
                    break
                field_exp[h + dh*i + 1][w + dw*i + 1] = -1
                i += 1

# 探索

from collections import deque

dq = deque()
dq.append([start[0]+1, start[1]+1, 0])
while dq:
    h, w, d = dq.popleft()
    if field_exp[h][w] != float('inf'):
        continue
    field_exp[h][w] = d
    for dh, dw in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        dq.append([h+dh, w+dw, d+1])

ans = field_exp[goal[0] + 1][goal[1] + 1]
if ans == float('inf'):
    print(-1)
else:
    print(ans)