from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
dd = defaultdict(int)
ans = 0
for i in range(N):
    now = A[-1-i]
    ans += i-dd[now]
    dd[now] += 1
print(ans)