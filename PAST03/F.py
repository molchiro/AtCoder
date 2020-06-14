N = int(input())
A = [list(input()) for _ in range(N)]
ans = ['']*N
f = True
for i in range((N+1)//2):
    s1 = set(A[i])
    s2 = set(A[-1-i])
    s3 = s1 & s2
    if s3:
        c = list(s3)[0]
        ans[i] = c
        ans[-1-i] = c
    else:
        f = False
        break
    
if f:
    print(*ans, sep='')
else:
    print(-1)