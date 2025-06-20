N, M = list(map(int, input().split()))
from atcoder.dsu import DSU

dsu = DSU(N)

# 繋がってないものはつなぎ、すでに繋がっていたならケーブルはとっとく
cables = []
f = 0
boss = -1 # 全てのサーバーの基準
for i in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    if f == 0 and not A == B:
        boss = A
    
    if dsu.same(A, B):
        cables.append((i, (A, B)))
        continue

    dsu.merge(A, B)

if boss == -1:
    boss = cables[0][1][0]

# 基準サーバーと同じグループか管理
boss_l = dsu.leader(boss)
connected = [0]*N
remaining = set()
for i in range(N):
    i_l = dsu.leader(i)
    if i_l == boss_l:
        connected[i] = 1
    else:
        remaining.add(i_l)

# print(boss_l)

# 残ったケーブルを繋ぎかえる
ans = []
while remaining:
    i, (a, b) = cables.pop()
    # print(i, a, b)
    # 両方とも基準グループにつながっているなら、片方をまだつながっていないグループに付け替える
    # print('dbug', dsu.leader(a), dsu.leader(b))
    if dsu.leader(a) == dsu.leader(boss_l) and dsu.leader(b) == dsu.leader(boss_l):
        x = remaining.pop()
    else:
        x = boss_l
        remaining.remove(dsu.leader(a))
    ans.append((i+1, b+1, x+1))
    dsu.merge(a, x)
    
    # print(remaining, ans)

print(len(ans))
for i, a, b in ans:
    print(i, a, b)