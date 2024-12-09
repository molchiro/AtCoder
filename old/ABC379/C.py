N, M = list(map(int, input().split()))
X = list(map(int, input().split()))
A = list(map(int, input().split()))

XA = list(zip(X, A))
XA.sort(reverse=True)

filled = N+1

ans = 0
for i in range(M):
    x, a = XA[i]

    diff = filled - x
    # print(x, a, diff)
    if diff != a:
        print(-1)
        exit()
    n = min(diff, a)
    ans += (n-1)*n//2
    filled -= n

    # print(filled)
    
if filled == 1:
    print(ans)
else:
    print(-1)