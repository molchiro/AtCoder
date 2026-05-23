N = int(input())
Ss = [input() for _ in range(N)]
m = max([len(s) for s in Ss])
for s in Ss:
    l = len(s)
    d = m-l
    print('.'*(d//2) + s + '.'*(d//2))