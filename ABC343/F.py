import dataclasses
from atcoder.segtree import SegTree


@dataclasses.dataclass
class Top:
    v: int
    n: int
    
    def __or__(self, other):
        if self.v > other.v:
            return self
        elif self.v == other.v:
            return Top(self.v, self.n+other.n)
        else:
            return other

@dataclasses.dataclass
class TopTwo:
    top: Top = Top(0, 0)
    second: Top = Top(-1, 0)
    
    def __or__(self, other):
        if self.top.v > other.top.v:
            return TopTwo(self.top, self.second | other.top)
        elif self.top.v == other.top.v:
            return TopTwo(self.top | other.top, self.second | other.second)
        else:
            return TopTwo(other.top, self.top | other.second)

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
seg = SegTree(lambda x, y: x | y, TopTwo(), [TopTwo(Top(a, 1)) for a in A])

for _ in range(Q):
    a, b, c = list(map(int, input().split()))
    if a == 1:
        seg.set(b-1, TopTwo(Top(c, 1)))
    else:
        ans = seg.prod(b-1, c)
        print(ans.second.n)