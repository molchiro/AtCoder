N, C = list(map(int, input().split()))
T = list(map(int, input().split()))

prev = -10**18
ans = 0
for t in T:
    if t-prev >= C:
        ans += 1
        prev = t
print(ans)