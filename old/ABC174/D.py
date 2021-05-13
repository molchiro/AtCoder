N = int(input())
C = input()
l = 0
r = N-1
ans = 0
while l < r:
    while l < r and C[l] == 'R':
        l += 1
    while l < r and C[r] == 'W':
        r -= 1
    if l >= r:
        break
    ans += 1
    l += 1
    r -= 1
print(ans)