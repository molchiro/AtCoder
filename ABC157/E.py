N = int(input())
S = [s for s in input()]
Q = int(input())
for i in range(Q):
    a, b, c = input().split()
    if a == '1':
        S[int(b)-1] = c
    else:
        print(len(set(S[int(b)-1:int(c)])))
