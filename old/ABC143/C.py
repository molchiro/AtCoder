N = int(input())
S = input()

ans = 0
tmp = ''
for s in S:
    if s != tmp:
        ans += 1
    tmp = s

print(ans)