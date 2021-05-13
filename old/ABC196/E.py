N = int(input())
# [left, rigth, C]
f = [-float('inf'), float('inf'), 0]
for _ in range(N):
    a, t = list(map(int, input().split()))
    if t == 1:
        f = [x+a for x in f]
    elif t == 2:
        f[0] = max(f[0], a)
        f[1] = max(f[1], a)
    else:
        f[0] = min(f[0], a)
        f[1] = min(f[1],a )
Q = int(input())
X = list(map(int, input().split()))
for x in X:
    x += f[2]
    print(min(f[1], max(x, f[0])))