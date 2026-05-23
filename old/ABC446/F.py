import sys
sys.setrecursionlimit(10**9)

class MinimumExcludant:
    # セグ木の実装とほぼ同様
    # 長さ N の非負整数列の mex は 0 以上 N 以下であることを利用した実装
    # N: updateが呼び出されうる回数（つまりmexの最大値となりうる数値）
    # updateに対してNを超える値が与えられた時、mexになり得ないので無視する
    def __init__(self, N):
        self.N = N
        self.next_pow_of_2 = 2**N.bit_length()
        self.tree = [0]*2*self.next_pow_of_2

    def update(self, x, val):
        if x > self.N:
            return
        k = self.next_pow_of_2 + x
        self.tree[k] = val
        while k > 1:
            k //= 2
            self.tree[k] = min(self.tree[2*k], self.tree[2*k+1])

    def increment(self, x, step=1):
        if x > self.N:
            return
        k = self.next_pow_of_2 + x
        self.update(x, self.tree[k] + step)
    
    def decrement(self, x, step=1):
        if x > self.N:
            return
        k = self.next_pow_of_2 + x
        self.update(x, self.tree[k] - step)

    def get(self):
        res = 1
        while res < self.next_pow_of_2:
            res *= 2
            if self.tree[res] != 0:
                res += 1

        return res - self.next_pow_of_2 


N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)

from collections import defaultdict

mex = MinimumExcludant(N)
stock = defaultdict(list)
deleted = set()
reached = [0]*N

# i番目まで処理している最中にuが新たに到達可能となった
def after_reach(i, u):
    global G, deleted, reached, mex
    # print('reach', u)

    for v in G[u]:
        # 到達してはいけない頂点は消す
        if v > i:
            deleted.add(v)
            stock[v].append(u)
        else:
            # 新たに到達可能な点が増えたなら再帰で処理
            if reached[v]:
                continue

            reached[v] = 1
            mex.increment(v)
            after_reach(i, v)

reached[0] = 1
mex.increment(0)
after_reach(0, 0)

for i in range(N):
    # print('deleted', deleted)
    # print('mex', mex.get())
    # 消されていたなら復活
    if i in deleted:
        deleted.remove(i)

        # 辺も復活
        for v in stock[i]:
            if reached[v] and reached[i] == 0:
                reached[i] = 1
                mex.increment(i)
                after_reach(i, i)


    if mex.get() == i+1:
        print(len(deleted))
    else:
        print(-1)
