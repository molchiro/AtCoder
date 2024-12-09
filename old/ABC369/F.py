H, W, N = list(map(int, input().split()))
coins = [list(map(int, input().split())) for _ in range(N)]

# R, Cについてソートしておくことで、Cに関するLISを見つける問題に帰着できる
coins.sort(lambda x: (x[0], x[1]))

d = [float('inf')]*N
idx = [None]*N
pre = [None]*N

from bisect import bisect_left, bisect_right

ans_n = 0
for i, (_, c) in enumerate(coins):
    x = bisect_right(d, c)
    d[x] = c
    idx[x] = i
    if x > 0:
        pre[i] = idx[x-1]

    if x+1 > ans_n:
        ans_n = x+1
        last = i

# 復元
move = [last]
while pre[move[-1]] != None:
    move.append(pre[move[-1]])

print(ans_n)
move = move[::-1]
now = (1, 1)
for coin in move:
    r, c = coins[coin]
    print('D'*(r-now[0]), end='')
    print('R'*(c-now[1]), end='')
    now = (r, c)

print('D'*(H-now[0]), end='')
print('R'*(W-now[1]), end='')
print()