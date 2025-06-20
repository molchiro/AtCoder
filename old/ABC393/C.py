N, M = list(map(int, input().split()))
seen = set()
ans = 0
for _ in range(M):
    u, v = list(map(int, input().split()))
    if u == v:
        ans += 1
        continue
    
    if u > v:
        u, v = v, u
    
    if (u, v) in seen:
        ans += 1
    
    seen.add((u, v))

print(ans)