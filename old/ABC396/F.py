# 初期回をセグ木で求める
# クエリをO(1)で捌く

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# 左側に自分以外の数が何個あるか
left = []
counter = [0]*M
for i, a in enumerate(A):
    left.append(i-counter[a])
    counter[a] += 1
# print(left)

# 右側に自分以外の数が何個あるか
right = []
counter = [0]*M
for i, a in enumerate(A[::-1]):
    right.append(i-counter[a])
    counter[a] += 1
right.reverse()
# print(right)

# あまりが0になるタイミングで値がどれだけ変化するか
d = {i: 0 for i in range(M)}
for i, a in enumerate(A):
    d[a] += left[i]
    d[a] -= right[i]

from atcoder.segtree import SegTree

st = SegTree((lambda x, y: x+y), 0, M+1)
ans = 0
for a in A:
    r = a%M
    st.set(r, st.get(r)+1)
    inversions = st.prod(r+1, M+1)
    ans += inversions

for i in range(M):
    print(ans)
    ans += d[(M-1-i)%M]