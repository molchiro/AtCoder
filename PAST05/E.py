H, W = list(map(int, input().split()))
field = [[-1]*30 for _ in range(30)]
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == '.':
            field[10+h][10+w] = 0

T = [[0]*W for _ in range(H)]
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == '#':
            T[h][w] = -1

# print(*field, sep='\n')
# print(*T, sep='\n')

for _ in range(4):
    for i in range(30-len(T)):
        for j in range(30-len(T[0])):
            # (j, i)を基準にチェック
            f = 0
            for h in range(len(T)):
                for w in range(len(T[0])):
                    dum = field[i+h][j+w]
                    dam = T[h][w]
                    if field[i+h][j+w]*T[h][w]:
                        f = 1
                if f:
                    break
            else:
                print('Yes')
                exit()
    # Tを回転
    T = T[::-1]
    T = list(map(list, zip(*T)))
print('No')