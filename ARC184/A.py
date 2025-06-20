N, M, Q = list(map(int, input().split()))

def print_ans(ans):
    print(*(['!'] + [str(x) for x in ans]))

# 11個ずつのブロックに分けて調査する
res_block = [[] for _ in range(91)]
for i in range(90):
    for j in range(10):
        print(f'? {i*11+1} {i*11+j+2}')
        res_block[i].append(int(input()))
# 最後のブロックは10個だけ
for j in range(9):
    print(f'? {991} {992+j}')
    res_block[-1].append(int(input()))

# ここまでで1が出てきていなければ残りの10個が偽と確定する
if sum([sum(x) for x in res_block]) == 0:
    print_ans([991 + i for i in range(10)])
    exit()

# 1が含まれないブロックは全て真であると確定できる
ok = None
for i in range(91):
    if sum(res_block[i]) == 0:
        ok = i*11 + 1
        break

ans = []
# 1が含まれているブロックの真贋を調査する
for i in range(91):
    if sum(res_block[i]) == 0:
        continue

    print(f'? {ok} {i*11+1}')
    f = int(input())
    if f:
        ans.append(i*11+1)
    for j, res in enumerate(res_block[i]):
        if res != f:
            ans.append(i*11+2+j)
print_ans(ans)

