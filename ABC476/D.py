N, M, K = list(map(int, input().split()))
X, Y = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

cumsum = [0]
for a in A:
    cumsum.append(a+cumsum[-1])

total = X + K*Y

ans = 0
ok = 0
ng = N+1
while ng - ok > 1:
    test = (ng+ok)//2
    if cumsum[test] <= total:
        ok = test
    else:
        ng = test
ans = ok

# Bを何種類目まで買うか総当たり
K_rem = Y
B_n = 0
for i in range(M):
    # 買えるなら買う
    if B[i] <= K*K_rem:
        m = (B[i]+K-1)//K
        K_rem -= m
        total -= B[i]
        B_n += 1

    # 残りのお金でAを買えるだけ買う
    ok = 0
    ng = N+1
    while ng - ok > 1:
        test = (ng+ok)//2
        if cumsum[test] <= total:
            ok = test
        else:
            ng = test
    # print(i, K_rem, ok, total)
    ans = max(ans, B_n+ok)

print(ans)