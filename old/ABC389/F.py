N = int(input())
contests = [list(map(int, input().split())) for _ in range(N)]

from atcoder.lazysegtree import LazySegTree



Q = int(input())
queries = list(map(tuple, enumerate(map(int, input().split()))))
queries.sort(key=lambda x: x[1])


def op(a, b):
    return max(a, b)
e = 0
def mapping(f, x):
    return max(f, x)
def composition(f, g):
    return max(f, g)

id = 0
seg = LazySegTree(op, e, mapping, composition, id, [v for i, v in queries])
