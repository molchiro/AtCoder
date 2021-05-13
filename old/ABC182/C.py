from collections import Counter

S = input()
C = Counter([int(x)%3 for x in S])
if C[0] == 0 and C[1] == 0 and C[2] < 3:
    print(-1)
elif C[0] == 0 and C[1] < 3 and C[2] == 0:
    print(-1)
else:
    digit_sum = sum([int(x) for x in S])
    if digit_sum%3 == 0:
        print(0)
    elif digit_sum%3 == 1:
        if C[1] > 0:
            print(1)
        else:
            print(2)
    else:
        if C[2] > 0:
            print(1)
        else:
            print(2)