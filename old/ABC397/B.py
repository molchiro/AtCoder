S = input()

ans = 0
if S[-1] == 'i':
    ans += 1
    
f = 0
for s in S:
    if f == 0 and s == 'i':
        f = 1
        continue
    if f == 1 and s == 'o':
        f = 0
        continue
    
    ans += 1


print(ans)