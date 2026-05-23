H, W = list(map(int, input().split()))
S = ''.join([input() for _ in range(H)])

# 状態遷移をうまく管理しながらBFS

from collections import deque

dq = deque()
dq.append((S, 0))
seen = set()

while dq:
    u, n = dq.popleft()

    # ゴミがなければそれまでの操作列の長さを返して終了
    if '#' not in u:
        print(n)
        exit()

    if u in seen:
        continue

    seen.add(u)

    # 現在の状態を一回り大きい2次元配列に展開
    field = [['.']*(W+2)] + [['.']+ ['.']*W + ['.'] for _ in range(H)] + [['.']*(W+2)]
    for h in range(H):
        for w in range(W):
            if u[h*W + w] == '#':
                field[h+1][w+1] = '#'
            if u[h*W + w] == 'T':
                now = (h, w)
    
    # 4方向試す
    for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_field = []
        for h in range(H):
            tmp = []
            for w in range(W):
                tmp.append(field[h+1+dh][w+1+dw])
            new_field.append(tmp)
        # 高橋を戻した時汚れるなら棄却
        if new_field[now[0]][now[1]] == '#':
            continue
        else:
            new_field[now[0]][now[1]] = 'T'
        # 新しい状態
        v = ''.join([''.join(row) for row in new_field])
        dq.append((v, n+1))

print(-1)