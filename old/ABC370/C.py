S = input()
T = input()
N = len(S)
X = []
while S != T:
    tmp = []
    for i in range(N):
        if S[i] != T[i]:
            tmp.append(S[:i] + T[i] + S[i+1:])
    tmp.sort()
    S = tmp[0]
    X.append(S)

print(len(X))
print(*X, sep='\n')