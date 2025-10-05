N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

masu = [0]*(N+2)
ans = 0
for a in A:
    if masu[a] == 0:
        x = masu[a-1] + masu[a+1]
        if x == 0:
            ans += 1
        elif x == 2:
            ans -= 1
    else:
        x = masu[a-1] + masu[a+1]
        if x == 0:
            ans -= 1
        elif x == 2:
            ans += 1
    masu[a] = (masu[a]+1)%2
    print(ans)