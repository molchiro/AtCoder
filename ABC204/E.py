from heapq import heapify, heappop, heappush

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C, D = list(map(int, input().split()))
    graph[A-1].append((B-1, C, D))
    graph[B-1].append((A-1, C, D))

min_t = [float('inf')]*N
hq = [(0, 0)]
while hq:
    t, u = heappop(hq)
    # print(u, t)
    if min_t[u] != float('inf'):
        continue
    min_t[u] = t
    for v, c, d in graph[u]:
        x = max(t, int(d**0.5)-3)
        t_ = float('inf')
        # print(x)
        for i in range(5):
            t_ = min(t_, (x+i)+c+int(d/(x+i+1)))
        heappush(hq, (t_, v))
# print(min_t)
ans = min_t[N-1]
if ans == float('inf'):
    ans = -1
print(ans)