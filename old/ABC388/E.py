N = int(input())
A = list(map(int, input().split()))

idx = N-2
ans = 0
for a in A[::-1]:
    while idx >= 0 and A[idx]*2 > a:
        idx -= 1

    if idx < 0:
        break

    ans += 1
    idx -= 1

print(ans)