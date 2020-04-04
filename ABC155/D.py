import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# 積がx未満となるペアの個数totがK個未満となるxの最大値を二分探索で求める
# lがOK,rがNG
l_x = -10**18 - 1
r_x = 10**18 + 1
while l_x + 1 < r_x:
    x = (l_x + r_x)//2
    tot = 0
    # 積がx未満となるペアの個数を求めてtotに追加する
    for i in range(N):
        a = A[i]
        if a > 0:
            n = bisect.bisect_left(A, (x+a-1)//a)
            tot += n
            if a*a < x:
                tot -= 1
        elif a < 0:
            n = bisect.bisect_right(A, (x+a-1)//a)
            tot += N-n
            if a*a < x:
                tot-= 1
        else:
            if x > 0:
                tot += N - 1
    tot /= 2
    if tot < K:
        l_x = x
    else:
        r_x = x
print(l_x)