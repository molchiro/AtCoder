N = int(input())
S = input()

ans = ''
f = 1
for s in S:
    if f and s == 'o':
        continue

    f = 0
    ans += s

print(ans)