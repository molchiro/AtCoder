N, A, B = list(map(int, input().split()))
S = input()
A_cumsum = [0]
B_cumsum = [0]
for s in S:
    A_cumsum.append(A_cumsum[-1])
    B_cumsum.append(B_cumsum[-1])
    if s == 'a':
        A_cumsum[-1] += 1
    else:
        B_cumsum[-1] += 1

# 右を固定した時にlが取りうる範囲をA,Bそれぞれでにぶたん
ans = 0
for r in range(N):
    if A_cumsum[r+1] < A:
        continue


    # aの個数がA以上となる時の最も右の位置
    ok = 0
    ng = r+1
    while ng - ok > 1:
        test = (ng+ok)//2
        if A_cumsum[r+1] - A_cumsum[test] >= A:
            ok = test
        else:
            ng = test
    rightest = ok

    # bの個数がB未満となる時の最も左の位置
    ng = -1
    ok = r
    while ok - ng > 1:
        test = (ok+ng)//2
        if test == -1:
            break
        if B_cumsum[r+1] - B_cumsum[test] < B:
            ok = test
        else:
            ng = test
    leftest = ok

    # print(r, rightest, leftest)
    ans += max(rightest - leftest + 1, 0)

print(ans)