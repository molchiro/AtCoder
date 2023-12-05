N, M = list(map(int, input().split()))
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))
G = [set() for _ in range(N)]
for a, b in zip(A, B):
    G[a].add(b)
    G[b].add(a)

from collections import deque

res = [-1]*N
seen = [0]*N
for i in range(N):
    if res[i] == -1:
        dq = deque([(i, 0)])
        while dq:
            u, b = dq.popleft()
            # print(u, b)
            if res[u] == -1:
                res[u] = b
            else:
                if res[u] != b:
                    print('No')
                    # print(u, res)
                    exit()
            if seen[u] == 0:
                seen[u] = 1
                for v in G[u]:
                    dq.append((v, (b+1)%2))

print('Yes')
