from collections import deque

dq = deque()

Q = int(input())
for _ in range(Q):
    ipt = input()
    if ipt[0] == '1':
        dq.append(ipt.split()[-1])
    else:
        print(dq.popleft())