from bisect import bisect_right

class MergeSortTree:
    def __init__(self, lst):
        # lstの長さより大きい最小の2のn乗を求め、その２倍のサイズのリストを初期値として持つ
        lst_len = len(lst)
        self.size = 2**(len('{:b}'.format(lst_len-1))+1)
        self.size_half = self.size//2
        self.sort_tree = [[0] for _ in range(self.size)]
        for i in range(lst_len):
            self.sort_tree[self.size_half + i][0] = lst[i]
        # 累積和の木も同様に初期化する
        self.cumsum_tree = [[0] for _ in range(self.size)]
        for i in range(self.size_half):
            self.cumsum_tree[self.size_half + i].append(self.sort_tree[self.size_half + i][0])
        # マージソートの容量でマージしながら親要素を作っていく
        for i in range(self.size_half-1, 0, -1):
            self.sort_tree[i] = sorted(self.sort_tree[i*2] + self.sort_tree[i*2+1])
            for e in self.sort_tree[i]:
                self.cumsum_tree[i].append(self.cumsum_tree[i][-1] + e)
    
    def query(self, l, r, x):
        # [l, r)
        l += self.size_half
        r += self.size_half
        res = 0
        while l < r:
            if l%2:
                idx = bisect_right(self.sort_tree[l], x)
                res += self.cumsum_tree[l][idx]
                l += 1
            if r%2:
                idx = bisect_right(self.sort_tree[r-1], x)
                res += self.cumsum_tree[r-1][idx]
            l //= 2
            r //= 2
        return res

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

MST = MergeSortTree(A)
# print(MST.sort_tree)
# print(MST.cumsum_tree)
ans = 0
for _ in range(Q):
    a, b, c = list(map(int, input().split()))
    l = a^ans
    l -= 1
    r = b^ans
    x = c^ans
    # print(l, r, x)
    ans = MST.query(l, r, x)
    print(ans)
