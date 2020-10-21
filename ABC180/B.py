N = int(input())
X = list(map(int, input().split()))
m = 0
y = 0
c = 0
for x in X:
    x_ = abs(x)
    m += x_
    y += x_**2
    c = max(c, x_)

y = pow(y, 0.5)
print(m)
print(y)
print(c)