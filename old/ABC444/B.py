N, K = list(map(int, input().split()))
ans = 0
for i in range(1, N+1):
    tmp = 0
    n = i
    while n:
        tmp += n%10
        n //= 10
    if tmp == K:
        ans += 1
print(ans)