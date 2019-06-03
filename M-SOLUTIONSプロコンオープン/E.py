Q = int(input())
for i in range(Q):
    x, d, n = list(map(int, input().split()))
    X = [x + (n-i-1)*d for i in range(n)]
    res = 1
    for x in X:
        res *= x
        res = res%1000003
    print(res)
