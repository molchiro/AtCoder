N = int(input())
S = input()


from atcoder.segtree import SegTree

# (i, j): Bがi個消費しきれてない、右にj個Aを使える

def op(ele1, ele2):
    l_i, l_j = ele1
    r_i, r_j = ele2
    # l_jを使ってr_iを処理
    if l_j >= r_i:
        # 余りをr_jにマージ
        return (l_i, r_j + (l_j-r_i))
    else:
        # 処理しきれないなら余りをl_iにマージ
        return (l_i + (r_i-l_j), r_j)


seg = SegTree(op, (0, 0), [(0, 1) if x == 'A' else (1, 0) for x in S])

Q = int(input())
for _ in range(Q):
    t, *params = input().split()
    if t == '1':
        i, c = params
        i = int(i)-1
        seg.set(i, (0, 1) if c == 'A' else (1, 0))
    else:
        l, r = params
        l = int(l)-1
        r = int(r)
        print('Yes' if seg.prod(l, r)[0] == 0 else 'No')