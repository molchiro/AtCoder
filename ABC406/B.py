N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 1
for a in A:
    ans *= a
    if ans > 10**(K)-1:
        ans = 1
print(ans)