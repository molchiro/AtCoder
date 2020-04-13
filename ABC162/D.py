from collections import Counter

N = int(input())
S = input()
RGB_Counter = Counter(S)
ans = RGB_Counter['R'] * RGB_Counter['G'] * RGB_Counter['B']

dum = []
d = 0
while 3 + d*2 <= N:
    for i in range(N - 2*(d+1)):
        a = S[i]
        b = S[i+d+1]
        c = S[i+2*(d+1)]
        if a != b and b != c and c != a:
            ans -= 1
    d += 1

print(ans)