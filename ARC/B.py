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
    
    def get_top_idx(self):
        top_el = self.tree[1]
        idx = 1
        while idx < self.next_pow_of_2:
            if self.tree[idx*2] == top_el:
                idx = idx*2
            else:
                idx = idx*2+1
        return idx - self.next_pow_of_2

INF = 10**7

N = int(input())
cards = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
seg_init = [INF]*400000
color = [[] for _ in range(400000)]
for i in range(N):
    a, b = cards[i]
    if seg_init[a] == INF:
        seg_init[a] = 0
    if seg_init[b] == INF:
        seg_init[b] = 0
    seg_init[a] += 1
    seg_init[b] += 1
    color[a].append(i)
    color[b].append(i)
ST = SegTree(seg_init, lambda x, y: min(x, y), INF)
seen_card = [0]*N
seen_color = [0]*400000

while ST.tree[1] != INF:
    target_color = ST.get_top_idx()
    seen_color[target_color] = 1
    target_colored_cards = color[target_color]
    for card in target_colored_cards:
        if seen_card[card] == 0:
            target_card = card
    seen_card[target_card] = 1
    # print(target_color, target_card)
    # input()
    for x in cards[target_card]:
        n = ST.get(x)
        if n == INF:
            continue
        if x == target_color or n == 1:
            ST.update(x, INF)
        else:
            ST.update(x, n-1)

print(sum(seen_color))