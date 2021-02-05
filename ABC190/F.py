class BIT:
    # 非負整数に対応するため、0-indexedで実装
    def __init__(self, size):
        self.size = size + 1
        self.data = [0]*self.size

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.data[i-1] += x
            i += i & -i
        
    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.data[i-1]
            i -= i & -i
        return res

N = int(input())
A = list(map(int, input().split()))

BIT_ = BIT(3*10**5)
total_invs = 0
for i, a in enumerate(A):
    total_invs += i - BIT_.sum(a)
    BIT_.add(a, 1)

for a in A:
    print(total_invs)
    total_invs += N - 2*a - 1