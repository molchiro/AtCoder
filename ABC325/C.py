class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]
    
H, W = list(map(int, input().split()))

ans = 0
field = [[0]*(W+1) for _ in range(H+1)]
for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == '#':
            field[h+1][w+1] = 1
        else:
            ans -= 1

UF = UnionFind(H*W)
for h in range(H):
    for w in range(W):
        for dh, dw in [(1, 1), (0, 1), (1, 0), (-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1)]:
            # print(h, w, dh,dw)
            if 0<=h+dh<H and 0<=w+dw<W and field[h+1][w+1] and field[h+1+dh][w+1+dw]:
                # print('unite')
                UF.unite(h*W+w, (h+dh)*W+w+dw)

# print(ans)
# print(UF.par)
s = set()
for h in range(H):
    for w in range(W):
        s.add(UF.root(h*W+w))
        # print(UF.root(h*W+w))

print(len(s)+ans)
