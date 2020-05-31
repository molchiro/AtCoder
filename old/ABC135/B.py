N = int(input())
P = list(map(int, input().split()))
P_ = sorted(P[:])
cnt = 0
for i in range(N):
    if P[i] != P_[i]:
        cnt += 1

if cnt < 3:
    print('YES')
else:
    print('NO')
