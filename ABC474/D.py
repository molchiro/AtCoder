LIM = 10**18

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []

t = 0
a = 0

for i in range(N):
    if A[i] > B[i]:
        ans.append(LIM)
        t += LIM*A[i]
        a += LIM*B[i]
    else:
        ans.append(1)
        t += A[i]
        a += B[i]

if t > a:
    print('Yes')
    print(*ans)
else:
    print('No')