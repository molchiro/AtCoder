import dataclasses

@dataclasses.dataclass
class UnionFind:
    N: int
    f: bool
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
    
    def unite(self, u: int, v: int) -> None:
        ru = self.root(u)
        rv = self.root(v)

        if ru == rv:
            return
        
        if ru > rv:
            ru, rv = rv, ru
        if self.f:
            ru, rv = rv, ru
        self.par[ru] += self.par[rv]
        self.par[rv] = ru


N, Q = list(map(int, input().split()))

uf_head = UnionFind(N, False)
uf_tail = UnionFind(N, True)
leader_c = [x for x in range(N)]

ans = [1]*N

for _ in range(Q):
    t, *query = list(map(lambda x: int(x) - 1, input().split()))
    if t == 0:
        x, c = query

        # 色を変える
        size = uf_head.size(x)
        head = uf_head.root(x)
        tail = uf_tail.root(x)
        # print(head, tail)
        ans[leader_c[head]] -= size
        ans[c] += size
        leader_c[head] = c

        # 先頭方向にマージできるかぎりマージ
        while head > 0:
            left_c = leader_c[uf_head.root(head-1)]
            if left_c != c:
                break

            uf_head.unite(head, head-1)
            uf_tail.unite(head, head-1)
            head -= 1


        # 末尾方向にマージできるかぎりマージ
        while tail < N-1:
            right_c = leader_c[uf_head.root(tail+1)]
            if right_c != c:
                break

            uf_head.unite(tail, tail+1)
            uf_tail.unite(tail, tail+1)
            tail += 1
        
        # print(query)
        # print(*uf_head.par)
        # print(*uf_tail.par)
        # print(leader_c)
        # print(ans)
        # print()
    else:
        c = query[0]
        print(ans[c])
