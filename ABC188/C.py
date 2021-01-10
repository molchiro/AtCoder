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
    
    def solve(self):
        top_el = self.tree[1]
        if self.tree[2] == top_el:
            semi_loser = 3
        else:
            semi_loser = 2
        idx = semi_loser
        value = self.tree[idx]
        while idx < self.next_pow_of_2:
            if self.tree[idx*2] == value:
                idx = idx*2
            else:
                idx = idx*2+1
        return idx - self.next_pow_of_2

N = int(input())
A = list(map(int, input().split()))
ST = SegTree(A, lambda x, y: max(x, y), 0)
print(ST.solve()+1)