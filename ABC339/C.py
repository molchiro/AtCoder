N = int(input())
A = list(map(int, input().split()))
ans = 0
now = 0
for a in A:
    now += a
    ans = min(ans, now)

print(-ans+now)