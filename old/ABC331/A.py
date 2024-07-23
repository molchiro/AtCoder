M, D = list(map(int, input().split()))
y, m, d = list(map(int, input().split()))
if d == D:
    d = 1
    m += 1
else:
    d += 1
if m > M:
    y += 1
    m = 1
print(y, m, d)