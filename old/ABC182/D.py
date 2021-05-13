N = int(input())
A = list(map(int, input().split()))
ans = 0
now = 0
accum = 0
extremun = 0
for a in A:
    accum += a
    extremun = max(extremun, accum)
    ans = max(ans, now+extremun)
    now += accum
print(ans)