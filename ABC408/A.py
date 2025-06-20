N, S = list(map(int, input().split()))
T = list(map(int, input().split()))
prev = 0
f = 1
for t in T:
    if t-prev > S:
        f = 0
    prev = t

print('Yes' if f else 'No')