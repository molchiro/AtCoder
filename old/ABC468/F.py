N = int(input())
P = list(map(int, input().split()))

ans = 0

dp = [10**18]*(N+1)
used = [-1]*N
dp[0] = P[0]
used[0] = 0
for i in range(1, N):
    p = P[i]
    if p < P[0]:
        continue
    ok = N
    ng = 0
    while ok - ng > 1:
        test = (ng+ok)//2
        if p < dp[test]:
            ok = test
        else:
            ng = test
    if ok <= 0:
        continue
    dp[ok] = p
    used[i] = ok

    # print(dp)
    # print(used)

while dp[-1] == 10**18:
    dp.pop()

ans += len(dp)

Q = []
prev = max(used)
for i in range(N-1, -1, -1):
    if used[i] == prev:
        prev -= 1
    else:
        Q.append(P[i])

Q = Q[::-1]
# print("Q", Q)

dp = [10**18]*(N+1)
for p in Q:
    ok = N
    ng = -1
    while ok - ng > 1:
        test = (ng+ok)//2
        if p <= dp[test]:
            ok = test
        else:
            ng = test
    dp[ok] = p

# print(dp)

while dp and dp[-1] == 10**18:
    dp.pop()

ans += len(dp)

print(ans)