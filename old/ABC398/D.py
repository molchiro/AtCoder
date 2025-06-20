from collections import defaultdict

N, R, C = list(map(int, input().split()))
S = input()
r, c = 0, 0

t = 0
d = defaultdict(lambda: float('inf'))
d[(r, c)] = min(d[(r, c)], t)
for s in S:
    t += 1
    if s == 'N':
        r -= 1
    elif s == 'S':
        r += 1
    elif s == 'W':
        c -= 1
    else:
        c += 1
    
    d[(r, c)] = min(d[(r, c)], t)

# print(d)

r, c = -R, -C
t = 0
ans = []
for s in S:
    t += 1
    if s == 'N':
        r -= 1
    elif s == 'S':
        r += 1
    elif s == 'W':
        c -= 1
    else:
        c += 1
    
    if t <= d[(r, c)]:
        ans.append(0)
    else:
        ans.append(1)

print(*ans, sep='')
