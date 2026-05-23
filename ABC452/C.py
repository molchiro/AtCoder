N = int(input())
seiyaku = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
S = [input() for _ in range(M)]

# f[何文字][何番目][文字]
f = [[[0]*26 for _ in range(11)] for _ in range(11)]

for s in S:
    for i, c in enumerate(s):
        f[len(s)][i+1][ord(c)-ord('a')] = 1

for s in S:
    if len(s) != N:
        print('No')
        continue

    ans = 1
    for i, c in enumerate(s):
        A, B = seiyaku[i]
        if f[A][B][ord(c)-ord('a')]:
            continue

        ans = 0
    
    print('Yes' if ans else 'No')