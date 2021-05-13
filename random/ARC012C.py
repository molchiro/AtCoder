from copy import deepcopy

B_original = [list(input()) for _ in range(19)]

# oの個数とxの個数が共に0なら正常
# oの個数とxの個数が同じなら、直前に打ったのはx
# oの個数がxの個数より一つ多いなら、直前に打ったのはo
# それ以外は異常なパターン
o_num = sum([x.count('o') for x in B_original])
x_num = sum([x.count('x') for x in B_original])
queue = []
if o_num == 0 and x_num == 0:
    print('YES')
    exit()
elif o_num - x_num == 0:
    for h in range(19):
        for w in range(19):
            if B_original[h][w] == 'x':
                queue.append((h, w))
elif o_num - x_num == 1:
    for h in range(19):
        for w in range(19):
            if B_original[h][w] == 'o':
                queue.append((h, w))
else:
    print('NO')
    exit()

# 一つ前の状態でどちらも勝利していないものがあれば成立
for h, w in queue:
    B = deepcopy(B_original)
    B[h][w] = '.'
    B_rotated = B[::-1]
    B_rotated = list(map(list, zip(*B_rotated)))
    B_diagonal = []
    for i in range(19):
        h, w = i, 0
        tmp = []
        tmp_rotated = []
        while h < 19 and w < 19:
            tmp += B[h][w]
            tmp_rotated.append(B_rotated[h][w])
            h += 1
            w += 1
        B_diagonal.append(tmp)
        B_diagonal.append(tmp_rotated)
    for i in range(19):
        h, w = 0, i
        tmp = []
        tmp_rotated = []
        while h < 19 and w < 19:
            tmp += B[h][w]
            tmp_rotated.append(B_rotated[h][w])
            h += 1
            w += 1
        B_diagonal.append(tmp)
        B_diagonal.append(tmp_rotated)

    B_all = B + B_rotated + B_diagonal

    for b in B_all:
        # print(b)
        if 'ooooo' in ''.join(b):
            break
        if 'xxxxx' in ''.join(b):
            break
    else:
        print('YES')
        exit()
print('NO')