S = input()
ans = ''
for s in S:
    if s in [str(i) for i in range(10)]:
        ans += s
print(ans)