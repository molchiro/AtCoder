mod = 998244353

T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))

    ans = 0
    for i, p in enumerate(P, 1):
        if p != i:
            break

        if i == N:
            ans += 1
        else:
           ans += N-i
    
    print(ans%mod)
        