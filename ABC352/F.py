import dataclasses

@dataclasses.dataclass
class UnionFindWidhPotentioal:
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

N, M = list(map(int, input().split()))
P = [[] for _ in range(N)]
seen = [0]*N
uf = UnionFindWidhPotentioal(N)
for _ in range(M):
    A, B, C = list(map(int, input().split()))
    uf.unite(A-1, B-1, C)
    seen[A-1] = 1
    seen[B-1] = 1

print(uf.parent)
print(uf.potential)