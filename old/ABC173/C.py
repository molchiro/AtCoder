from itertools import product

H, W, K = list(map(int, input().split()))
# 黒なら1
board = [[1 if x == '#' else 0 for x in list(input())] for _ in range(H)]

ans = 0
# 塗らないなら1
for row in product([0, 1], repeat=H):
    for col in product([0, 1], repeat=W):
        # 元が黒でタテヨコ塗らないマスを数える
        blacks = sum([board[h][w] * row[h] * col[w] for h in range(H) for w in range(W)])
        if blacks == K:
            ans += 1
print(ans)
