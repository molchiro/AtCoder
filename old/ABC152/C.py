N = int(input())
P = list(map(int, input().split()))
m = 200001
ans = 0
for p in P:
    if p < m:
        ans += 1
        m = p
print(ans)