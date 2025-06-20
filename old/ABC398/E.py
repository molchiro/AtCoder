from collections import deque

N = int(input())
edges = set()
for i in range(N-1):
    for j in range(i+1, N):
        edges.add((i, j))

G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    if a > b:
        a, b = b, a
    G[a].append(b)
    G[b].append(a)
    edges.discard((a, b))

def judge(s, g):
    global N, G

    seen = set()
    dq = deque()
    dq.append((s, 0))
    while dq:
        u, d = dq.popleft()

        if u == g:
            return d%2 == 1
        
        if u in seen:
            continue

        seen.add(u)

        for v in G[u]:
            if v in seen:
                continue
            dq.append((v, d+1))

can_select = set()
for s, g in edges:
    if judge(s, g):
        can_select.add((s, g))

if len(can_select)%2:
    print('First')
    me = 1
else:
    print('Second')
    me = 0

while True:
    if me:
        u, v = can_select.pop()
        print(u+1, v+1)
        me = 0
    else:
        u, v = list(map(lambda x: int(x) - 1, input().split()))
        
        if u > v:
            u, v = v, u
        
        if (u, v) == (-2, -2):
            break
        
        can_select.discard((u, v))
        me = 1

