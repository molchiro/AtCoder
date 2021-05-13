from collections import deque

N, M = list(map(int, input().split()))
to = [[] for _ in range(N)]
for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    to[A].append(B)
    to[B].append(A)

ans = [None]*N
ans[0] = 0

queue = deque()
queue.append(0)
while queue:
    x = queue.popleft()
    connected = to[x]
    for u in connected:
        if ans[u] == None:
            ans[u] = x + 1
            queue.append(u)
print('Yes')
print(*ans[1:], sep='\n')
