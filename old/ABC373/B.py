S = input()
ans = 0
u = S.index('A')
for x in 'BCDEFGHIJKLMNOPQRSTUVWXYZ':
    v = S.index(x)
    ans += abs(v-u)
    u = v
print(ans)