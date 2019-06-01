r, D, x = list(map(int, input().split()))

for i in range(10):
    x = x*r -D
    print(x)