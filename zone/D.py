from collections import deque
S = input()
R = 0
T = deque()
for s in S:
    if s == 'R':
        R ^= 1
    else:
        if len(T):
            if R:
                if s == T[0]:
                    T.popleft()
                else:
                    T.appendleft(s)
            else:
                if s == T[-1]:
                    T.pop()
                else:
                    T.append(s)
        else:
            T.append(s)
if R:
    T = list(T)[::-1]
print(''.join(T))