offset = 10**8
ofof = offset*offset
ofofof = offset*ofof

H, W = list(map(int, input().split()))
field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == 'S':
            S = (h+1, w+1)
        elif row[w] == 'G':
            G = (h+1, w+1)
        elif row[w] == '#':
            field[h+1][w+1] = -1

# print(*field, sep='\n')

seen = set()

from collections import deque

dq = deque()
# f==0のとき、直前に横移動
dq.append(S[0]*ofofof + S[1]*ofof + 0*offset + 0)
dq.append(S[0]*ofofof + S[1]*ofof + 1*offset + 0)

while dq:
    node = dq.popleft()

    d = node%offset
    node //= offset

    if node in seen:
        continue
    seen.add(node)

    f = node%offset
    node //= offset
    w = node%offset
    node //= offset
    h = node

    # print(h, w, f, d, seen)

    if (h, w) == G:
        print(d)
        exit()

    if f:
        for dw in (1, -1):
            if field[h][w+dw] == -1:
                continue
            
            dq.append(h*ofofof + (w+dw)*ofof + 0*offset + (d+1))
    else:
        for dh in (1, -1):
            if field[h+dh][w] == -1:
                continue
            
            dq.append((h+dh)*ofofof + (w)*ofof + 1*offset + (d+1))

print(-1)