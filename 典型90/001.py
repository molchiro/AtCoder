N, L = list(map(int, input().split()))
K = int(input())
A = [0] + list(map(int, input().split())) + [L] + [float('inf')]
ok = 1
ng = 10**9
while ng-ok > 1:
    center = (ok+ng)//2
    prev = 0
    n = 0
    for i in range(K+1):
        l = prev
        r = N+2
        while r-l > 1:
            m = (l+r)//2
            if A[m]-A[prev] >= center:
                r = m
            else:
                l = m
        if r >= N+2:
            break
        n += 1
        prev = r
        if n >= K+1:
            break
        
    if n >= K+1:
        ok = center
    else:
        ng = center

print(ok)

                