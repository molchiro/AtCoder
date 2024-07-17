N, L, R = list(map(int, input().split()))
R += 1
next_pow_of_R = 1
while next_pow_of_R < R:
    next_pow_of_R *= 2


from collections import deque, defaultdict

dq = deque([R])
G = defaultdict(list)
seen = set()

while dq:
    # print(dq)
    now = dq.popleft()
    if now == L:
        break
    if now in seen:
        continue
    seen.add(now)

    d = 1
    while now%d == 0 and d < next_pow_of_R:
        if now - d >= 0:
            if now - d not in seen:
                dq.append(now-d)
                G[now].append(now-d)
        if now+d < next_pow_of_R:
            if now + d not in seen:
                dq.append(now+d)
                G[now].append(now+d)
        
        d *= 2

# print(G)

prev = dict()
dq = deque()
dq.append(R)
while dq:
    # print(dq)
    u = dq.popleft()
    if u == L:
        break
    for v in G[u]:
        if v in prev:
            continue
        prev[v] = u
        dq.append(v)

# print(prev)

ans = 0
u = L
while u != R:
    v = prev[u]
    if u < v:
        i = 0
        while 2**i < v-u:
            i += 1
        j = u//(2**i)
        print('?', i, j)
        ans += int(input())
        ans %= 100
        u = v
    else:
        i = 0
        while 2**i < u-v:
            i += 1
        j = v//(2**i)
        print('?', i, j)
        ans -= int(input())
        ans %= 100
        u = v

print('!', ans)