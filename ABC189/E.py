from collections import deque

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
OP = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
QL = []
for i in range(Q):
    a, b = list(map(int, input().split()))
    QL.append((a, b-1, i))
QL.sort(key=lambda x:x[0])

dq = deque(QL)

ans = [[] for _ in range(Q)]
dim = 0
px = 1
qx = 0
py = 1
qy = 0
for i in range(M+1):
    while dq:
        if dq[0][0] != i:
            break
        a, b, n = dq.popleft()
        x, y = B[b]

        x = px*x + qx
        y = py*y + qy
        for _ in range(dim):
            x, y = -y, x
        ans[n] = [x, y]
    if not dq:
        break
    op = OP[i]
    # print(op)
    if op[0] == 1:
        dim = (dim-1)%4
    elif op[0] == 2:
        dim = (dim+1)%4
    else:
        p = op[0]-3
        p -= dim
        p %= 4
        if p == 0:
            px *= -1
            qx = 2*op[1] - qx
        elif p == 1:
            py *= -1
            qy = 2*op[1] - qy
        elif p == 2:
            px *= -1
            qx = -2*op[1] - qx
        else:
            py *= -1
            qy = -2*op[1] - qy

# print(ans)
for i in range(Q):
    x, y = ans[i]
    print(x, y)