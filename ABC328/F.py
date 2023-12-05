import dataclasses

@dataclasses.dataclass
class UnionFind:
    N: int
    parent: list[int] = dataclasses.field(init=False)
    potential: list[int] = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        self.parent = [-1]*self.N
        self.potential = [0]*self.N
    
    def root(self, u: int) -> int:
        # 負数だった場合が自分がroot
        if self.parent[u] < 0:
            return u

        # 経路圧縮
        prev_par = self.parent[u]
        self.parent[u] = self.root(self.parent[u])
        self.potential[u] += self.potential[prev_par]
        return self.parent[u]
    
    def size(self, u):
        return -self.parent[self.root(u)]
    
    def is_same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)
    
    def unite(self, u: int, v: int, p: int) -> None:
        # u -> v 方向のポテンシャルの増分をpとする
        ru = self.root(u)
        rv = self.root(v)
        # サイズが小さい方を大きい方に従属させる
        if self.size(ru) > self.size(rv):
            u, v = v, u
            ru, rv = rv, ru
            p *= -1
        self.parent[rv] += self.parent[ru]
        self.potential[ru] = p + self.potential[v] - self.potential[u]
        self.parent[ru] = rv

N, Q = list(map(int, input().split()))
UF = UnionFind(N)
ans = []
for i in range(Q):
    a, b, d = list(map(lambda x: int(x) - 1, input().split())) # 
    d += 1
    if UF.is_same(a, b):
        if UF.potential[b] - UF.potential[a] == d:
            ans.append(i+1)
    else:
        UF.unite(b, a, d)
        ans.append(i+1)
    
    # print(UF.parent)
    # print(UF.potential)

print(' '.join(map(str, ans)))