from atcoder.segtree import SegTree

N = int(input())
st = SegTree(lambda x, y: x+y, 0, 2*N)
for _ in range(N):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    if A > B:
        A, B = B, A
    if st.prod(A, B) != 0:
        print('Yes')
        break
    st.set(A, 1)
    st.set(B, -1)
else:
    print('No')
