N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_preserved = A[:]
B_preserved = B[:]

active = [i for i in range(N)]
final = [(i, a, b) for i, (a, b) in enumerate(zip(A, B))]
print(final)
queries = [list(map(int, input().split())) for _ in range(Q)]
query_res = []
for q, (t, i, x) in enumerate(queries):
    i -= 1
    if t == 1:
        A[i] = x
    else:
        B[i] = x
    pre = active[i]
    nxt = N+i
    active[i] = nxt
    query_res.append((pre, nxt))
    final.append((q+N, A[i], B[i]))
print(final)
final.sort(key=lambda x: -x[-1])

from atcoder.lazysegtree import LazySegTree

e = (0, -10**18) # (a: 書き始める時間, b: a+届くまでの時間) 
id = 0
def op(x, y):
    return (y[0], max(x[1], y[1]))
def mapping(f, x):
    return (f+x[0], f+x[1])
def composition(f, g):
    return f+g

tmp = 0
v = []
d = [None]*(N+Q)
for i, (idx, a, b) in enumerate(final):
    d[idx] = i
    if i < N:
        tmp += a
        v.append((tmp, tmp+b))
    else:
        v.append((tmp, -10**10))
# print(v)
seg = LazySegTree(op, e, mapping, composition, id, v)


print(d, final)
A = A_preserved
B = B_preserved
for q in range(Q):
    _, i, x = queries[q]
    i -= 1
    pre, nxt = query_res[q]
    pre_i = d[pre]
    nxt_i = d[nxt]

    # preを無効化
    seg.apply(pre, N+Q, -A[i])
    seg.set(pre, (seg.get(pre_i)[0], -10**18))
    
    i -= 1
    if t == 1:
        A[i] = x
    else:
        B[i] = x

    # nxtを有効化
    seg.apply(nxt, N+Q, A[i])
    seg.set(nxt, (seg.get(pre_i)[0], seg.get(pre_i)[0]+B[i]))

    print(seg.all_prod()[0])

    
