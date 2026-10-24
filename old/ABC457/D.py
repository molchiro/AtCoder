N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

def condition(X):
    global N, K, A

    ct = 0
    for i, a in enumerate(A, start=1):
        if a < X:
            ct += ((X-a)+i-1)//i
    
    # print(X, ct)
    
    return ct <= K

ok = min(A)
ng = 10**30
while ng - ok > 1:
    test = (ng+ok)//2
    if condition(test):
        ok = test
    else:
        ng = test

print(ok)