def sign(x):
    return 0 if abs(x) == 0 else x // abs(x)

T = int(input())
for _ in range(T):
    A, B, X, Y = list(map(int, input().split()))
    m, M = min(abs(X), abs(Y)), max(abs(X), abs(Y))
    ans = 0
    # 斜め移動
    ans += 2*min(A, B)*m
    # 残り
    if abs(X) > abs(Y):
        
        ans += min(A, B*3)*((M-m+1)//2)
        ans += min(B, A*3)*((M-m)//2)
    else:
        ans += min(B, A*3)*((M-m+1)//2)
        ans += min(A, B*3)*((M-m)//2)

    
    print(ans)