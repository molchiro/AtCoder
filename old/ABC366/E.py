N, D = list(map(int, input().split()))
offset = 10**6+10

count_x = [0]*(4*offset)
count_y = [0]*(4*offset)
d_x = [0]*(4*offset)
d_y = [0]*(4*offset)

for _ in range(N):
    X, Y = list(map(int, input().split()))
    count_x[X+2*offset] += 1
    count_y[Y+2*offset] += 1
    d_x[0] += X+2*offset
    d_y[0] += Y+2*offset

l = 0
u = N
for i in range(1, 4*offset):
    d_x[i] = d_x[i-1] + l - u
    l += count_x[i]
    u -= count_x[i]

l = 0
u = N
for i in range(1, 4*offset):
    d_y[i] = d_y[i-1] + l - u
    l += count_y[i]
    u -= count_y[i]

d_y_min = min(d_y)
ans = 0
l = 0
u = 4*offset-2
for x in range(4*offset):
    d1 = d_x[x]
    if d1 > D:
        continue
    d2 = D - d1
    while not (d_y[l] <= d2 and d_y[l-1] > d2):
        if d_y[l] > d2:
            if d_y[l] == d_y_min:
                break
            l += 1
        else:
            l -= 1
    while not (d_y[u] <= d2 and d_y[u+1] > d2):
        if d_y[u] > d2:
            if d_y[u] == d_y_min:
                break
            u -= 1
        else:
            u += 1

    if d_y_min <= d2:
        ans += u-l+1
    # print(l, u)

print(ans)
