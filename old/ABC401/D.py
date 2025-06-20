N, K = list(map(int, input().split()))
S = list(input())

if N == 1:
    if K == 1:
        print('o')
    else:
        print(S[0])
    exit()

for i in range(N):
    s = S[i]
    if s == 'o':
        K -= 1
        continue
    elif s == '.':
        continue

    if i == 0:
        if S[1] == 'o':
            S[0] = '.'
    elif i == N-1:
        if S[-2] == 'o':
            S[-1] = '.'
    else:
        if S[i-1] == 'o' or S[i+1] == 'o':
            S[i] = '.'

units = []
accum = ''
for s in S:
    if s == '?':
        if type(accum) is str:
            units.append(accum)
            accum = 1
        else:
            accum += 1
    else:
        if type(accum) is str:
            accum += s
        else:
            units.append(accum)
            accum = s
units.append(accum)
# print(units)
if K == 0:
    for i in range(len(units)):
        if type(units[i]) is str:
            continue

        units[i] = '.'*units[i]


elif sum([(x+1)//2 for x in units if type(x) is int]) == K:
    for i in range(len(units)):
        if type(units[i]) is str:
            continue

        if units[i] % 2:
            units[i] = ''.join(['.' if j%2 else 'o' for j in range(units[i])])
        else:
            units[i] = '?'*units[i]
else:
    for i in range(len(units)):
        if type(units[i]) is str:
            continue

        units[i] = '?'*units[i]


print(''.join(units))