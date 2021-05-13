N = int(input())
f = [0]*(N+1)
f[0] = 1

ans = -1
for _ in range(N):
    A = int(input())
    if f[A]:
        ans = A
    f[A] = 1

if ans == -1:
    print('Correct')
else:
    print(ans, f.index(0))
