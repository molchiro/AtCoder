class SegTree:
    def __init__(self, init_list):
        self.id_el = 0
        self.seg_func = lambda x, y: x | y
        n = len(init_list)
        self.next_pow_of_2 = 2**(n-1).bit_length()

        self.tree = [self.id_el]*2*self.next_pow_of_2
        for i in range(n):
            self.tree[self.next_pow_of_2 + i] = 1 << init_list[i]
        for i in range(self.next_pow_of_2 - 1, 0, -1):
            self.tree[i] = self.seg_func(self.tree[2*i], self.tree[2*i+1])
    
    def query(self, l, r):
        l += self.next_pow_of_2
        r += self.next_pow_of_2
        res = self.id_el
        while l < r:
            if l%2 == 1:
                res = self.seg_func(res, self.tree[l])   
                l //= 2
                l += 1
            else:
                l //= 2
            
            if r%2 == 0:
                res = self.seg_func(res, self.tree[r])
                r //= 2
                r -= 1
            else:
                r //= 2
            print(l, r, res)
        if l == r:
            res = self.seg_func(res, self.tree[l])
        return res

N, Q = list(map(int, input().split()))
C = list(map(lambda x: int(x) - 1, input().split()))
ST = SegTree(C)
for _ in range(Q):
    l, r = list(map(lambda x: int(x) - 1, input().split()))
    print(ST.query(l, r))
print(ST.tree)