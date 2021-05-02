N, D, H = list(map(int, input().split()))
ans = 0
for _ in range(N):
    d, h = list(map(int, input().split()))
    ans = max(ans, H-D/(D-d)*(H-h))
print(ans)