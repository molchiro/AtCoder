A, R, N = list(map(int, input().split()))

ans = A
large = False
N -= 1
while N > 0:
    if N & 1 == 1:
        ans *= R
    if ans > 10**9:
        large = True
        break
    R *= R
    N = N >> 1

if large:
    print('large')
else:
    print(ans)