H, W = list(map(int, input().split()))
total = 0
min_A = float('inf')
for _ in range(H):
    A = list(map(int, input().split()))
    min_A = min(min_A, *A)
    total += sum(A)

print(total - min_A * H * W)