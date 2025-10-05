H, W = list(map(int, input().split()))

field = [[99]*(W+2)] + [[99]+ [0]*W + [99] for _ in range(H)] + [[99]*(W+2)]

l = []
for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == '#':
            l.append((h+1, w+1))

ans = 0
while l:
    ans += len(l)
    # 変化のあったセルを覚えながら塗る
    changed = set()
    for h, w in l:
        field[h][w] = 99
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            field[h+dh][w+dw] += 1
            if field[h+dh][w+dw] == 1:
                changed.add((h+dh, w+dw))

    # 次ターンに塗るリストを更新
    l = []
    # 変化のあったセルの中が丁度1かチェック
    for h, w in changed:
        if field[h][w] == 1:
            l.append((h, w))

print(ans)
