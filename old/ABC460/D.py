H, W = list(map(int, input().split()))
S = []
for _ in range(H):
    row = [1 if c == '#' else 0 for c in input()]
    S.append(row)

def encode(field):
    res = ''
    for row in field:
        for x in row:
            res += '#' if x else '.'
    return res

def act():
    global H, W, S, G

    res = []
    for h in range(H):
        row = []
        for w in range(W):
            if S[h][w] == 1:
                row.append(0)
                continue

            tmp = 0
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                nh = h+dh
                nw = w+dw
                if 0 <= nh < H and 0 <= nw < W:
                    tmp += S[nh][nw]
            
            row.append(min(tmp, 1))
        res.append(row)
    
    # print(*res, sep='\n')
    # print('-----------')
    
    return res

# ループを検出するまでグラフを構築

G = dict()
prev_hash = encode(S)
seen = set()
array = [prev_hash]
while True:
    nS = act()
    hash = encode(nS)
    G[prev_hash] = hash
    if hash in seen:
        loop_s = hash
        break
    seen.add(hash)
    prev_hash = hash
    array.append(hash)
    S = nS

# print(G)
# print(array)
loop_at = array.index(loop_s)
loop_len = len(array)-loop_at
# print('loop starts ', loop_at, ', size', loop_len)

ans_idx = loop_at + (10**100 - loop_at)%loop_len

# print(array[ans_idx])
ans = array[ans_idx]
for h in range(H):
    for w in range(W):
        print(ans[h*W+w], end='')
    print()