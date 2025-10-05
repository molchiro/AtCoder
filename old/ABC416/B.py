S = input()
f = 0
ans = ''
for s in S:
    if not f and s == '.':
        ans += 'o'
        f = 1
    else:
        ans += s

    if s == '#':
        f = 0
print(ans)