N = int(input())

S = input()

ans = 10**18


# ABパターン
target = 1
tmp = 0
for i, s in enumerate(S):
    if s == 'B':
        tmp += abs(target-i)
        target += 2
ans = min(ans, tmp)

# ABパターン
target = 0
tmp = 0
for i, s in enumerate(S):
    if s == 'B':
        tmp += abs(target-i)
        target += 2
ans = min(ans, tmp)

print(ans)