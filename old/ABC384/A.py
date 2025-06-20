N, c1, c2 = input().split()
S = input()
ans = ''
for s in S:
    if s == c1:
        ans += s
    else:
        ans += c2
print(ans)