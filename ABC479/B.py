N = int(input())
S = input()
tmp = 0
ans = 0
for s in S:
    if s == 'R':
        tmp += 1
    else:
        tmp = 0
    ans = max(ans, tmp)
print(ans)