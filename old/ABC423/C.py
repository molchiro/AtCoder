N, R = list(map(int, input().split()))
L = list(map(int, input().split()))

ans = 0

# 左側の回数
l = 0
f = 0
accum = 0
for i in range(R):
    if f == 0:
        if L[i] == 1:
            l += 1
        else:
            f = 1
    else:
        if L[i] == 1:
            accum += 1
ans += accum
ans += R-l

# print(ans)

# 右側の個数
r = N
f = 0
accum = 0
for i in range(N-1, R-1, -1):
    if f == 0:
        if L[i] == 1:
            r -= 1
        else:
            f = 1
    else:
        if L[i] == 1:
            accum += 1
ans += accum
ans += r-R

print(ans)
        