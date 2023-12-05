N, K = list(map(int, input().split()))
X, Y = map(list, zip(*[list(map(int, input().split())) for _ in range(N)]))
X.sort()
Y.sort()
print(X)
print(Y)

ok = max(X[-1]-X[0], Y[-1]-Y[0])
ng = -1
while ok - ng > 1:
    test = (ok+ng)//2
    cost = 0
    # x方向のシミュレーション
    
    # y方向のシミュレーション
    if cost <= K:
        ok = test
    else:
        ng = test