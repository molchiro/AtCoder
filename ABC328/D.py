S = input()

from collections import deque

dq = deque(['', ''])
for s in S:
    dq.append(s)
    if dq[-3] == 'A' and dq[-2] == 'B' and dq[-1] == 'C':
        dq.pop()
        dq.pop()
        dq.pop()
print(''.join(dq))