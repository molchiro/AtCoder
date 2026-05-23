from collections import defaultdict

mod = 10007
K, M = list(map(int, input().split()))

G = dict()
size_d = defaultdict(int)
seen = set()

prev = 0
rem = 0
# node: (prev, c, ans.val())

def define_size(u):
    global G, size_d
    # print(G)

    if size_d[u] > 0:
        return size_d[u]

    seen_ = set()
    ct = 0
    now = u
    while True:
        ct += 1
        v = G[now]
        if v in seen_:
            break
        seen_.add(v)
        now = v
        
    seen_ = set()
    now = u
    while True:
        size_d[now] = ct
        v = G[now]
        if v in seen_:
            break
        seen_.add(v)
        now = v
    
    return ct

for _ in range(K):
    c, l = list(map(int, input().split()))
    now = (prev, c, rem)
    # 地道パート
    while l and now not in seen:
        # print(c, l, now)

        seen.add(now)
        l -= 1

        prev, c, rem = now
        x = prev * 10 + c
        r = x // M
        q = x % M
        rem = rem * 10 + r
        rem %= mod 
        nxt = (q, c, rem)
        G[now] = nxt
        now = nxt


    # ワープパート
    if now in seen:
        size = define_size(now)
        l %= size

    # 残りパート
    while l:
        l -= 1

        prev, c, rem = now
        x = prev * 10 + c
        r = x // M
        q = x % M
        rem = rem * 10 + r
        rem %= mod 
        nxt = (q, c, rem)
        G[now] = nxt
        now = nxt
    
    prev, _, rem = now

print(rem)
