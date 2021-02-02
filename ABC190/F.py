N = int(input())
A = list(map(lambda x: int(x) + 1, input().split()))

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
  
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
bit = Bit(3*10**5+10)
ans = 0
 
for i, a in enumerate(A):
    bit.add(a, 1)
    ans += i + 1 - bit.sum(a)
 
print(ans)

for i in range(N-1):
    a = A[i]
    ans -= a
    ans += N-a+1
    print(ans)