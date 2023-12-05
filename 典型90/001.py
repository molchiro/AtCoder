N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split())) + [L]
ok = 1
ng = L+1
while ok + 1 < ng:
    center = (ok+ng)//2
    prev = 0
    ct = 0
    for a in A:
        if a - prev >= center:
            prev = a
            ct += 1
    if ct >= K+1:
        ok = center
    else:
        ng = center
print(ok)