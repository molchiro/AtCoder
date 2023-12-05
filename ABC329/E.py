from collections import deque


N, M = list(map(int, input().split()))
S = input()
T = input()
dq = deque()
for i in range(N-M+1):
    if S[i:i+M] == T:
        dq.append(i)
check = list(S)
while dq:
    u = dq.popleft()
    if not 0 <= u <= N-M:
        continue
    U = ''.join(check[u:u+M])
    if U == '#'*M:
        continue
    if all([x == y or x == '#' for x, y in zip(list(U), list(T))]):
        for i in range(M):
            check[u+i] = '#'
        for i in range(1, M):
            dq.append(u+i)
            dq.append(u-i)

if all([x == '#' for x in check]):
    print('Yes')
else:
    print('No')
