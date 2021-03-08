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

    def add(self, idx, val):
        k = self.next_pow_of_2 + idx
        self.tree[k] += val
        while k > 1:
            k //= 2
            self.tree[k] = self.seg_func(self.tree[2*k], self.tree[2*k+1])
    
    def query(self):
        res = 1
        while res < self.next_pow_of_2:
            res *= 2
            if self.tree[res] != 0:
                res += 1
        return res - self.next_pow_of_2

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

ST = SegTree([0]*(N+1), lambda x, y: min(x, y), id_el=float('inf'))

for i in range(M):
    ST.add(A[i], 1)

# print(ST.tree)

ans = ST.query()
# print(ans)

for i in range(1, N-M+1):
    ST.add(A[i+M-1], 1)
    ST.add(A[i-1], -1)
    ans = min(ST.query(), ans)
    # print(ST.tree)

print(ans)