A, B = list(map(int, input().split()))

ans = float('inf')
d = float('inf')
for i in range(500):
    if abs(A/B - i) < d:
        ans = i
        d = abs(A/B - i)
        # print(i, d)
print(ans)