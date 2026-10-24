N = int(input())
S = list(map(int, input().split()))
seen = set(S)
T = list(map(int, input().split()))
for t in T:
    seen.add(t)

pairs = list(zip(S, T))
pairs.sort(key=lambda x: x[1])

print(pairs)


compressed = {}
for i, v in enumerate(sorted(list(seen))):
    compressed[v] = i

# print(compressed)

from atcoder.lazysegtree import LazySegTree

def op(a, b):
    return max(a, b)
e = 0
def mapping(f, x):
    return f+x
def composition(f, g):
    return f+g

id = 0
seg = LazySegTree(op, e, mapping, composition, id, len(seen))

ans = 0
for s, t in pairs:
    u = compressed[s]
    v = compressed[t]
    if u > v:
        # 移動量を補正したい
        ans += s-t

    else:
        # 移動量を補正したい
        ans += t-s
        # さらにすでに処理済みのやつらで動いちゃった個数を補正したい
        # ↑処理済み列でにぶたんできそう