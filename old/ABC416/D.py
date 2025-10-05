T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = 0
    for b in B:
        while A and A[-1]+b < M:
            ans += A.pop()
        
        if A:
            ans += (A.pop()+b)%M
        else:
            ans += b
    print(ans)