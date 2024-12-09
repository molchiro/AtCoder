N, M = list(map(int, input().split()))
s = set()

for _ in range(M):
    a, b = list(map(int, input().split()))
    s.add((a, b))
    for da, db in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        if 0 < a+da <= N and 0 < b+db <= N:
            s.add((a+da, b+db))

print(N**2-len(s))
