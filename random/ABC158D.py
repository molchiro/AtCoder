from collections import deque

S = deque(list(input()))
Q = int(input())
reverse = True
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        reverse = not reverse
    else:
        right = query[1] == '1'
        if right == reverse:
            S.appendleft(query[2])
        else:
            S.append(query[2])
if not reverse:
    print(''.join(list(reversed(S))))
else:
    print(''.join(list(S)))
