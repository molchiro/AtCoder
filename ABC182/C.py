from collections import Counter

S = input()
C = Counter([str(int(x)%3) for x in S])
if C['0'] == 0 and C['1'] == 0 and C['2'] < 3:
    print(-1)
elif C['0'] == 0 and C['1'] < 3 and C['2'] == 0:
    print(-1)
else:
    ans = min(abs(C['1']%3 - C['2']%3), abs(C['1'] - C['2'])%3)
    print(ans)