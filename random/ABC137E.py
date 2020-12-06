from collections import deque

N, M, P = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N)]

for e in edges:
    a, b, c = e
    graph[a-1].append(e)

q = deque(graph[0])
checked = [False]*N
edges = []
while q:
    e = q.pop()
    a, b, c = e
    if checked[a-1]:
        continue
    checked[a-1] = True
    edges.append(e)
    q.extend(graph[b-1])

M = len(edges)

score = [-float('inf')]*N
score[0] = 0

for i in range(N-1):
    for j in range(M):
        a, b, c = edges[j]
        if score[a-1] + c - P > score[b-1]:
            score[b-1] = score[a-1] + c - P 

ans = score[N-1]

for i in range(N-1):
    for j in range(M):
        a, b, c = edges[j]
        if score[a-1] + c - P > score[b-1]:
            score[b-1] = score[a-1] + c - P

print(max(ans, 0) if ans == score[N-1] else -1)