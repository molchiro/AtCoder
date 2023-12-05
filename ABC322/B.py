N, M = list(map(int, input().split()))
S = input()
T = input()
p = T[:N] == S
s = T[M-N:] == S

if p and s:
    print(0)
elif p:
    print(1)
elif s:
    print(2)
else:
    print(3)