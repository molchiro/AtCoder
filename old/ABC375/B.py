def euclidian_d(u, v):
    return ((u[0]-v[0])**2 + (u[1]-v[1])**2)**0.5

N = int(input())
u = (0, 0)
ans = 0
for _ in range(N):
    v = list(map(int, input().split()))
    ans += euclidian_d(u, v)
    u = v

v = (0, 0)
ans += euclidian_d(u, v)
    
print(ans)