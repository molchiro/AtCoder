Q, K = list(map(int, input().split()))
queries = []
X = set()
for _ in range(Q):
    t, x = list(map(int, input().split()))
    queries.append((t, x))
    X.add(x)

X = list(X)
X.sort()
idx_d = {x: i for i, x in enumerate(X)}
N = len(X)
print(X,)
print(idx_d)

lim = 10**20

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
    
    def query_l(self, x):
        x += self.next_pow_of_2
        if self.tree[x] == 0:
            return 0
        
        l = x
        while self.tree[l//2]:
            l //= 2
        while l < self.next_pow_of_2:
            l *= 2

        if l > self.next_pow_of_2 and self.tree[l-1]:
            l -= 1

        return l
    
    def query_r(self, x):
        x += self.next_pow_of_2
        if self.tree[x] == 0:
            return 0

        r = x
        while self.tree[r//2]:
            r //= 2
        while r < self.next_pow_of_2:
            r *= 2
            r += 1

        if r < self.next_pow_of_2*2 - 1 and self.tree[r+1]:
            r += 1


        return r 
    

sg_l = SegTree([0]*N,lambda x, y: x&y, 0 )
sg_r = SegTree([0]*N,lambda x, y: x&y, 0 )

f = [0]*N

for t, x in queries:
    if t == 1:
        idx = idx_d[x]
        f[idx] = 1
        if idx > 0:
            if x - X[idx-1] <= K:
                sg_l.update(idx, 1)
        if idx < N-1:
            if X[idx+1] - x <= K:
                sg_r.update(idx, 1)
    else:
        print(sg_r.query_r(x) - sg_l.query_l(x))
