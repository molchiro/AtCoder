W, B = list(map(int, input().split()))
n = 0
while W*1000 >= n*B:
    n += 1
print(n)