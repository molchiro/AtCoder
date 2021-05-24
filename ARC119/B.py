N = int(input())
S = input()
T = input()

ct_10 = 0
ct_01 = 0
ans = 0
for i in range(N):
    Si = S[i]
    Ti = T[i]
    if Si == '1' and Ti == '1':
        continue
    elif Si == '0' and Ti == '0':
        if ct_10 == ct_01:
            continue
        else:
            ans += 1
    else:
        if Si == '1':
            ct_10 += 1
        else:
            ct_01 += 1
        if ct_10 == ct_01:
            ans += ct_10
            ct_10 = 0
            ct_01 = 0

if ct_10 + ct_01 == 0:
    print(ans)
else:
    print(-1)        