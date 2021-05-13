from collections import deque
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    G[A].append(B)
    G[B].append(A)

def farthest(s):
    global N
    global G
    dq = deque()
    dq.append((s, 0))
    seen = [0]*N
    while dq:
        v, d = dq.popleft()
        seen[v] = 1
        for to in G[v]:
            if seen[to]:
                continue
            dq.append((to, d+1))
    return v, d

print(farthest(farthest(0)[0])[1]+1)