from bisect import bisect_left, bisect_right
N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()

for _ in range(Q):
    b, k = list(map(int, input().split()))

    ok = 0
    ng = 10**18
    while ng - ok > 1:
        test = (ng+ok)//2
        n = bisect_left(A, b+test) - bisect_right(A, b-test) 
        if n < k:
            ok = test
        else:
            ng = test
    print(ok)