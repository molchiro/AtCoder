N  = int(input())
A = list(map(int, input().split()))
INF = 10**18
over = False
ans = 1
for a in A:
    ans *= a
    if ans > INF:
        over = True
        break
if 0 in A:
    print(0)
elif over:
    print(-1)
else:
    print(ans)