N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 0
seat = 0
for a in A:
    if seat + a <= K:
        seat += a
    else:
        ans += 1
        seat = a
if seat > 0:
    ans += 1
print(ans)