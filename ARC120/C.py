from collections import defaultdict
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

    def update(self, idx, val):
        k = self.next_pow_of_2 + idx
        self.tree[k] = val
        while k > 1:
            k //= 2
            self.tree[k] = self.seg_func(self.tree[2*k], self.tree[2*k+1])
    
    def query(self, l, r):
        l += self.next_pow_of_2
        r += self.next_pow_of_2
        res = self.id_el
        while l < r:
            if l%2:
                res = self.seg_func(res, self.tree[l])
                l += 1
            if r%2:
                res = self.seg_func(res, self.tree[r-1])
            l //= 2
            r //= 2
        return res
    
    def get(self, idx):
        return self.tree[self.next_pow_of_2 + idx]

# dで要素の出現位置を管理
# lで要素の出現数を管理
# idxで各要素を何個目まで使ったか管理
# usedで使用済みの位置と個数を管理

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = [i+A[i] for i in range(N)]
B = [i+B[i] for i in range(N)]

d = defaultdict(list)
l = defaultdict(int)
for i, a in enumerate(A):
    d[a].append(i)
    l[a] += 1

idx = defaultdict(int)

used = SegTree([0]*N, lambda x, y: x+y, 0)

ans = 0
for i, b in enumerate(B):
    # 使用可能なbがなければ失敗
    if idx[b]+1 > l[b]:
        print(-1)
        exit()
    # bがAのどこにあるか探す
    j = d[b][idx[b]]
    idx[b] += 1
    used.update(j, 1)
    # bより右に表れたusedの個数分右にずらす
    # exp: [,,,used,x,b,y,used,z,used] => [,,,x,b,y,z] のとき+2
    j += used.query(j+1, N)
    # ansを更新
    ans += abs(j-i)

print(ans)