class MinimumExcludant:
    # セグ木の実装とほぼ同様
    # 長さ N の非負整数列の mex は 0 以上 N 以下であることを利用した実装
    # N: updateが呼び出されうる回数（つまりmexの最大値となりうる数値）
    # updateに対してNを超える値が与えられた時、mexになり得ないので無視する
    def __init__(self, N):
        self.N = N
        self.next_pow_of_2 = 2**N.bit_length()
        self.tree = [0]*2*self.next_pow_of_2

    def update(self, x, val):
        if x > self.N:
            return
        k = self.next_pow_of_2 + x
        self.tree[k] = val
        while k > 1:
            k //= 2
            self.tree[k] = min(self.tree[2*k], self.tree[2*k+1])

    def increment(self, x, step=1):
        if x > self.N:
            return
        k = self.next_pow_of_2 + x
        self.update(x, self.tree[k] + step)
    
    def decrement(self, x, step=1):
        if x > self.N:
            return
        k = self.next_pow_of_2 + x
        self.update(x, self.tree[k] - step)

    def get(self):
        res = 1
        while res < self.next_pow_of_2:
            res *= 2
            if self.tree[res] != 0:
                res += 1

        return res - self.next_pow_of_2 
