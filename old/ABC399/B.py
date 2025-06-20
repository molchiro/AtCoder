N = int(input())
P = list(map(int, input().split()))
rem = N
ans = [-1]*N
r = 1
while rem > 0:
    m = max(P)
    ct = 0
    for i, p in enumerate(P):
        if p == m:
            ans[i] = r
            ct += 1
            P[i] = 0
    
    rem -= ct
    r += ct

print(*ans, sep='\n')