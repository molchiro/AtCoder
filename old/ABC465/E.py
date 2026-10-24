from atcoder.modint import Modint, ModContext

mod = 998244353
with ModContext(mod):
    N = input()
        
    # state: (q, s) q: 3で割った余り, s 使った数字のビット列集合
    def encode(state):
        q, s = state
        return q * 10000 + s
    def decode(code):
        return (code//10000, code%10000)
    L = encode((2, 1024)) + 1

    # N未満の集合を管理
    dp = [Modint(0) for _ in range(L)]
    # N桁目までをなぞった時の状態を管理。中身はdpと同じ
    N_code = encode((0, 0))

    def new_code(crr_code, selected):
        q, s = decode(crr_code)
        return encode(((q*10 + selected)%3, s | 1<<selected))

    for i, ch in enumerate(N):
        digit = int(ch)
        ndp = [Modint(0) for _ in range(L)]
        
        # Nをなぞる
        n_N_code = new_code(N_code, digit)
        
        # NをなぞっていたところからN未満集合に落とす
        if i > 0:
            for n in range(digit):
                ndp[new_code(N_code, n)] += 1
        
        # leading-0からの遷移
        limit = 10 if i > 0 else digit # i==0の時だけN未満が確定していないので天井が異なる
        for n in range(1, limit):
            ndp[new_code(encode((0, 0)), n)] += 1

        # 通常の遷移
        for q in range(3):
            for s in range(1<<10):
                crr_code = encode((q, s))
                for n in range(10):
                    ndp[new_code(crr_code, n)] += dp[crr_code]

        dp = ndp
        N_code = n_N_code

    dp[N_code] += 1
    ans = Modint(0)
    for code in range(L):
        q, s = decode(code)
        f_i = q==0
        f_j =(s>>3)&1
        f_k = s.bit_count() == 3
        if f_i + f_j + f_k == 1:
            ans += dp[code]

    print(ans.val())