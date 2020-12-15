L = int(input())
ans = 1
for i in range(L-12+11, L-12, -1):
    ans *= i
for i in range(1, 12):
    ans //= i
print(ans)