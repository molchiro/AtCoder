H, W = list(map(int, input().split()))
S = [input() for _ in range(H)]

class union_find:
    def __init__(self, N):
        self.par = [i for i in range(N)]
    
    def root(self, i):
        if self.par[i] == i:
            return i
        else:
            # 経路圧縮
            self.par[i] = self.root(self.par[i])
            return self.par[i]
    
    def same(self, a, b):
        return self.root(a) == self.root(b)
    
    def unite(self, a, b):
        if not self.same(a, b):
            self.par[self.root(a)] = self.root(b)

UF = union_find(H+W)

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            UF.unite(h, H+w)
UF.unite(0, H)
UF.unite(0, H+W-1)
UF.unite(H-1, H)
UF.unite(H-1, H+W-1)

row = set()
for i in range(H):
    row.add(UF.root(i))
col = set()
for i in range(W):
    col.add(UF.root(H+i))

print(min(len(row)-1, len(col)-1))
