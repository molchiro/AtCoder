N, M = list(map(int, input().split()))
ans = 0
while M > 0:
    x = N%M
    M = x
    ans += 1
print(ans)