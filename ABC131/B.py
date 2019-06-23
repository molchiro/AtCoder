N, L = list(map(int, input().split()))

loss = float('inf')
total = 0
for i in range(N):
    x = L + i
    total += x
    if abs(x) < abs(loss):
        loss = x
print(total - loss)