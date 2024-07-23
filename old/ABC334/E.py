# import sys

# sys.setrecursionlimit(10**9)


H, W = list(map(int, input().split()))
field = [[0]*(W+2)] + [[0]+ [0]*W + [0] for _ in range(H)] + [[0]*(W+2)]
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == '#':
            field[h+1][w+1] = 1

from atcoder.dsu import DSU

dsu = DSU((H+2)*(W+2))

def flatten(h, w):
    global H
    global W
    return h*(W+2)+w


for h in range(H):
    for w in range(W):
        if field[h+1][w+1]:
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if field[h+1+dh][w+1+dw]:
                    # print('flatten(h+1, w+1), flatten(h+1+dh, w+1+dw)',h, w, dh, dw, flatten(h+1, w+1), flatten(h+1+dh, w+1+dw))
                    dsu.merge(flatten(h+1, w+1), flatten(h+1+dh, w+1+dw))

unions = set()
for h in range(H):
    for w in range(W):
        if field[h+1][w+1]:
            unions.add(dsu.leader(flatten(h+1, w+1)))
unions = len(unions)

MOD = 998244353
ans = 0
accum = 0
for h in range(H):
    for w in range(W):
        if field[h+1][w+1] == 0:
            accum += 1
            roots = set()
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if field[h+1+dh][w+1+dw]:
                    roots.add(dsu.leader(flatten(h+1+dh, w+1+dw)))
            ans += unions - (len(roots) - 1)
            ans %= MOD

from atcoder.math import inv_mod
print(ans*inv_mod(accum, MOD)%MOD)