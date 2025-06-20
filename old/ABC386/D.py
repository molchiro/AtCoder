N, M = list(map(int, input().split()))

offset = 10**10

queries_B = []
queries_W = []
for _ in range(M):
    X, Y, C = input().split()
    x = int(X)-1
    y = int(Y)-1
    if C == 'B':
        queries_B.append(x*(offset)+y)
    else:
        queries_W.append((y, x))

queries_B.sort(reverse=True)
queries_W.sort(reverse=True)

# print(queries_B)

b_events = []
c = -1
for q in queries_B:
    x = q//(offset)
    y = q%offset
    if y < c:
        continue
    b_events.append((y, x))
    c = y

# print(b_events)

f = 1
x_lim = -1
for y, x in queries_W:
    while b_events and b_events[-1][0] >= y:
        _, tmp = b_events.pop()
        x_lim = tmp
    
    if x <= x_lim:
        f = 0

print('Yes' if f else 'No')