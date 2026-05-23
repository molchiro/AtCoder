N, M = list(map(int, input().split()))
S = input()
T = input()
Q = int(input())
for _ in range(Q):
    w = input()
    t = 1
    a = 1
    for s in w:
        if s not in S:
            t = 0
        if s not in T:
            a = 0
        
    if a == 0:
        print('Takahashi')
    elif t == 0:
        print('Aoki')
    else:
        print('Unknown')