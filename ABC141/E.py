N = int(input())
S = input()
f = False
if len(set(S)) == N:
    print(0)
else:
    for i in range(N//2, 1, -1):
        for j in range(N - i):
            if S[j:j+i] in S[j+i:]:
                f = True
                break
        if f:
            print(i)
            break