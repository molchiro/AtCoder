N, M, P = list(map(int, input().split()))
ans = 0
i = 0
while M+P*i <= N:
    ans += 1
    i += 1
print(ans)