from collections import deque

N, M = list(map(int, input().split()))
roads = [[] for _ in range(N)]
for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    roads[A].append(B)
ans = 0
for i in range(N):
    seen = [0]*N
    dq = deque()
    dq.append(i)
    while dq:
        u = dq.popleft()
        if seen[u]:
            continue
        seen[u] = 1
        for v in roads[u]:
            dq.append(v)
    ans += sum(seen)
print(ans)

int