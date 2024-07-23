N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

idx = 0
ans = 0

for b in B:
    if idx == N:
        print(-1)
        exit()
    while A[idx] < b:
        idx += 1
        if idx == N:
            print(-1)
            exit()
    
    ans += A[idx]
    idx += 1


print(ans)