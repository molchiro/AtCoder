N = int(input())
d = {}
for i in range(N):
    S = input()
    if S in d:
        d[S] += 1
    else:
        d[S] = 1
M = max(d.values())
keys = [k for k, v in d.items() if v == M]
keys.sort()
for key in keys:
    print(key)