from sortedcontainers import SortedSet, SortedList, SortedDict

N, Q = list(map(int, input().split()))

import dataclasses

@dataclasses.dataclass
class UnionFind:
    N: int
    par: list[SortedSet] = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        self.par = [SortedSet([i]) for i in range(self.N)]
    
    def root(self, u: int) -> int:

        if type(self.par[u]) is SortedSet:
            return u

        # 経路圧縮
        self.par[u] = self.root(self.par[u])
        return self.par[u]

    def merge(self, u: int, v: int) -> None:
        # par
        ru = self.root(u)
        rv = self.root(v)
        if ru == rv:
            return
        if len(self.par[ru]) < len(self.par[rv]):
            ru, rv = rv, ru

        self.par[ru] |= self.par[rv]
        self.par[rv] = ru

UF = UnionFind(N)

for _ in range(Q):
    a, b, c = list(map(lambda x: int(x) - 1, input().split()))
    if a == 0:
        UF.merge(b, c)
        # print(*UF.par)
    else:
        ss = UF.par[UF.root(b)]
        if len(ss) < c+1:
            print(-1)
        else:
            print(ss[-c-1]+1)