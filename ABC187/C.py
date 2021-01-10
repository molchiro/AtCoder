from collections import defaultdict

N = int(input())

d = defaultdict(str)

for _ in range(N):
    S = input()
    if S[0] == '!':
        if d[S[1:]] == 0:
            d[S[1:]] = 2
        elif d[S[1:]] == 2:
            continue
        else:
            d[S[1:]] = 1
    else:
        if d[S] == 1:
            d[S] = 2
        elif d[S] == 2:
            continue
        else:
            d[S] = 0

for key in d.keys():
    if d[key] == 2:
        print(key)
        exit()
print('satisfiable')