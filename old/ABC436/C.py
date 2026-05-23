N, M = list(map(int, input().split()))

placed = set()

ans = 0
for _ in range(M):
    f = 1
    r, c = list(map(int, input().split()))
    for dr in range(2):
        for dc in range(2):
            if (r+dr, c+dc) in placed:
                f = 0
    
    if f:
        ans += 1
        for dr in range(2):
            for dc in range(2):
                placed.add((r+dr, c+dc))
print(ans)

