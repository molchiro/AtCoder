T = int(input())
for _ in range(T):
    N = int(input())

    # まずNを超えない最大の辺の長さを探る
    ok = 1
    ng = 10**10
    while ng - ok > 1:
        test = (ng+ok)//2
        if test**2 <= N:
            ok = test
        else:
            ng = test
    base = 2*ok*(ok-1)
    if ok**2 == N:
        print(base)
        # print('pattern1', base)
    elif ok*(ok+1) >= N:
        rem = N-ok*ok
        print(base + rem + (rem-1))
        # print('pattern2', ok, base + rem + (rem-1))
    else:
        rem = N-ok*(ok+1)
        print(base + ok + (ok-1) + rem + (rem-1))
        # print('pattern3', base + ok + (ok-1) + rem + (rem-1))

