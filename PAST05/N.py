class SegTree:
    def __init__(self, init_list, seg_func, id_el):
        self.id_el = id_el
        self.seg_func = seg_func
        n = len(init_list)
        self.next_pow_of_2 = 2**(n-1).bit_length()

        self.tree = [self.id_el]*2*self.next_pow_of_2
        for i in range(n):
            self.tree[self.next_pow_of_2 + i] = init_list[i]
        for i in range(self.next_pow_of_2 - 1, 0, -1):
            self.tree[i] = self.seg_func(self.tree[2*i], self.tree[2*i+1])

    def find_rightest(self, a, b, x, func, k=1, l=None, r=None):
        if l is None:
            l = self.next_pow_of_2
        if r is None:
            r = 2*self.next_pow_of_2
        # 探す範囲 [a, b)
        # 探す値 x
        # この再起で対象にしている頂点 k
        # 頂点kの範囲[l, r)
        # print('k', k, l, r)
        # 範囲外
        if r <= a + self.next_pow_of_2 or b + self.next_pow_of_2 <= l:
            return -1
        # 満たす値が無い
        if func(x, self.tree[k]) == False:
            return -1
        # 葉にたどり着いた(見つかった)
        if k >= self.next_pow_of_2:
            return k - self.next_pow_of_2
        # 右に優先的に降りる
        right_ans = self.find_rightest(a, b, x, func, k*2+1, (l+r)//2, r)
        if right_ans > 0:
            return right_ans
        # 左に降りる
        left_ans = self.find_rightest(a, b, x, func, k*2, l, (l+r)//2)
        return left_ans

    def find_leftest(self, a, b, x, func, k=1, l=None, r=None):
        if l is None:
            l = self.next_pow_of_2
        if r is None:
            r = 2*self.next_pow_of_2
        # 探す範囲 [a, b)
        # 探す値 x
        # この再起で対象にしている頂点 k
        # 頂点kの範囲[l, r)
        # print('k', k, l, r)
        # 範囲外
        if r <= a + self.next_pow_of_2 or b + self.next_pow_of_2 <= l:
            return -1
        # 満たす値が無い
        if func(x, self.tree[k]) == False:
            return -1
        # 葉にたどり着いた(見つかった)
        if k >= self.next_pow_of_2:
            return k - self.next_pow_of_2
        # 左に優先的に降りる
        left_ans = self.find_leftest(a, b, x, func, k*2, l, (l+r)//2)
        if left_ans > 0:
            return left_ans
        # 右に降りる
        right_ans = self.find_leftest(a, b, x, func, k*2+1, (l+r)//2, r)
        return right_ans

N, Q = list(map(int, input().split()))
L = []
R = []
for _ in range(N-1):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

L_segtree = SegTree(L, lambda x, y:max(x, y), 0)
R_segtree = SegTree(R, lambda x, y:min(x, y), 10**9)

for _ in range(Q):
    A, B = list(map(int, input().split()))

    l1 = L_segtree.find_rightest(0, B-1, A, lambda x, e: e > x)
    l2 = R_segtree.find_rightest(0, B-1, A, lambda x, e: e < x)
    if l1 == -1:
        l1 = 0
    else:
        l1 += 1
    if l2 == -1:
        l2 = 0
    else:
        l2 += 1
    l = max(l1, l2)

    r1 = L_segtree.find_leftest(B-1, N-1, A, lambda x, e: e > x)
    if r1 == -1:
        r1 = N-1
    r2 = R_segtree.find_leftest(B-1, N-1, A, lambda x, e: e < x)
    if r2 == -1:
        r2 = N-1
    r = min(r1, r2)

    # print(l1, l2, r1, r2)
    print(r-l+1)