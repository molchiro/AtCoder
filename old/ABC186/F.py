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

H, W, M = list(map(int, input().split()))
hrz = [[H] for _ in range(W+1)]
vrt = [[W] for _ in range(H+1)]
for _ in range(M):
    X, Y = list(map(lambda x: int(x) - 1, input().split()))
    hrz[Y].append(X)
    vrt[X].append(Y)
hrz[W].append(0)
vrt[H].append(0)

ans = sum([min(x) for x in hrz[:min(vrt[0])]])

init_list = [0 if i < min(vrt[0]) else 1 for i in range(W+1)]
st = SegTree(init_list, lambda x, y: x+y, 0)
for h in range(1, min(hrz[0])):
    ans += st.query(0, min(vrt[h]))
    for w in vrt[h]:
        st.update(w, 1)

print(ans)
