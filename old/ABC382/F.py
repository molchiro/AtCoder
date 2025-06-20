from atcoder.lazysegtree import LazySegTree

H, W, N = list(map(int, input().split()))

bars = []
for i in range(N):
    R, C, L = list(map(int, input().split()))
    bars.append((R, C, L, i))
bars.sort()

def op(a, b):
    return max(a, b)
e = 0
def mapping(f, x):
    return max(f, x)
def composition(f, g):
    return max(f, g)

id = 0
seg = LazySegTree(op, e, mapping, composition, id, W)

ans = [None]*N
while bars:
    r, c, l, i = bars.pop()

    # print('debug', r, c, l, i)

    tmp = seg.prod(c-1, c+l-1)
    ans[i] = H-tmp
    seg.apply(c-1, c+l-1, tmp+1)

    # print('debug', *[seg.get(j) for j in range(W)])

print(*ans, sep='\n')