mod = 998244353

class mod_comb:
    def __init__(self, max_n, mod):
        # modが素数でなければならないことに注意して使う
        self.mod = mod

        # x!を計算
        tmp = 1
        self.factorials = [tmp]
        for i in range(max_n):
            tmp *= i+1
            tmp %= mod
            self.factorials.append(tmp)
        # x!^-1を計算
        self.inverses = [None]*(max_n+1)
        tmp = pow(self.factorials[max_n], mod-2, mod)
        self.inverses[max_n] = tmp
        for i in range(max_n, 0, -1):
            tmp *= i
            tmp %= mod
            self.inverses[i-1] = tmp
        
    def get(self, n, r):
        if r > n or r < 0:
            return 0
        return self.factorials[n]*self.inverses[r]*self.inverses[n-r]%self.mod

if __name__ == "__main__":
    nCr_mod = mod_comb(5*10**6, mod)

    X1, X2, X3 = list(map(int, input().split()))

    ans = 0

    # ２をしきりとすると、X2 + 1 この区間がある。その中からkを選び、そこには1を一つ以上配置するとする
    for k in range(1, X2+1+1):
        # k個の区間を選ぶ
        tmp = nCr_mod.get(X2+1, k)
        # 1を置く場所を選ぶ
        tmp *= nCr_mod.get(X1-1, k-1)
        tmp %= mod
        # X2 + 1 - k の残りの区間の位置に3を0個以上配置する
        tmp *= nCr_mod.get(X2 - k + X3, X2 - k)
        tmp %= mod

        ans += tmp
        ans %= mod

    print(ans)
