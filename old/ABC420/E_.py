import dataclasses

@dataclasses.dataclass
class UnionFind:
    N: int
    par: list[int] = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        self.par = [-1]*self.N
    
    def root(self, u: int) -> int:
        # 負数だった場合が自分がroot
        if self.par[u] < 0:
            return u

        # 経路圧縮
        self.par[u] = self.root(self.par[u])
        return self.par[u]
    
    def size(self, u):
        return -self.par[self.root(u)]
    
    def is_same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)
    
    def unite(self, u: int, v: int) -> None:
        ru = self.root(u)
        rv = self.root(v)
        if ru == rv:
            return
        # サイズが小さい方を大きい方に従属させる
        if self.size(ru) > self.size(rv):
            u, v = v, u
            ru, rv = rv, ru
        self.par[rv] += self.par[ru]
        self.par[ru] = rv