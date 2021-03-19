# UFして個数を数える
# ループを持っているものが有効
# 2^n-1が答え

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

N = int(input())
f_list = list(map(lambda x: int(x) - 1, input().split()))
UF = union_find(N)
for i, to in enumerate(f_list):
    UF.unite(i, to)
roots = set()
for i in range(N):
    roots.add(UF.root(i))
print((2**len(roots)-1)%998244353)