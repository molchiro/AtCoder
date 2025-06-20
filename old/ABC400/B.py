N, M = list(map(int, input().split()))
ans = 0
now = 1
for _ in range(M+1):
    ans += now
    now *= N
    if ans > 1000000000:
        print('inf')
        break
else:
    print(ans)