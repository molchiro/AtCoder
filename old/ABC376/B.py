N, Q = list(map(int, input().split()))

L, R = 0, 1
ans = 0
for _ in range(Q):
    H, T = input().split()
    T = int(T)-1

    # 動かす手をLに固定
    if H == 'R':
        R, L = L, R

    offset = L

    # Lを原点とした相対座標に変換
    L = 0
    R -= offset
    T -= offset
    R %= N
    T %= N

    if R > T:
        L += T
        ans += T
    else:
        L -= N-T
        ans += N-T
         
    # 絶対座標に戻す
    L += offset
    R += offset
    L %= N
    R %= N

    # 動かす手を変えていたら戻す
    if H == 'R':
        R, L = L, R

print(ans)