N, Q = list(map(int, input().split()))
history = [(N-i, 0) for i in range(N)]

for _ in range(Q):
    t, u = input().split()
    if t == '1':
        x, y = history[-1]
        dx, dy = {'R': (1, 0), 'U':(0, 1), 'D': (0, -1), 'L': (-1, 0)}[u]
        history.append((x+dx, y+dy))
    else:
        print(*history[-int(u)])
