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
    nCr_mod = mod_comb(10**6, 10**9+7)
    print(nCr_mod.get(5, 2))
    print(nCr_mod.get(10**6, 5*10**5+1))