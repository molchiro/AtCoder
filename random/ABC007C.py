from collections import deque

R, C = list(map(int, input().split()))
S = list(map(lambda x: int(x) - 1, input().split()))
G = list(map(lambda x: int(x) - 1, input().split()))
maze = [input() for _ in range(R)]
cost = [[-1]*C for _ in range(R)]
cost[S[0]][S[1]] = 0
q = deque([S])
while q:
    y, x = q.popleft()
    for dx, dy in[[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < C and 0 <= ny < R):
            continue
        if maze[ny][nx] == '#':
            continue
        if cost[ny][nx] != -1:
            continue
        cost[ny][nx] = cost[y][x] + 1
        deque.append(q, [ny, nx])
print(cost[G[0]][G[1]])