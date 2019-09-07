N = int(input())
H = list(map(int, input().split()))
M = 0
left = 0
n = 0
for h in H:
    if h <= left:
        n += 1
    else:
        n = 0
    M = max(M, n)
    left = h
print(M)
