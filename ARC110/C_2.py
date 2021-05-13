N = int(input())
P = list(map(int, input().split()))

target = 1
ans = []
P_ = []
for i in range(1, N):
    if P[i] == target:
        P_.append(target)
        P_ += P[target-1:i-1]
        P[i] = P[i-1]
        ans += [j for j in range(i, target-1, -1)]
        target = i+1
P_.append(P[-1])
if P_ == [i+1 for i in range(N)] and len(ans) == N-1:
    print(*ans, sep='\n')
else:
    print(-1)