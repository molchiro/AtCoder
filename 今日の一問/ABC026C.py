N = int(input())
B = [int(input()) for i in range(N-1)]
S = [1 for i in range(N)]
for i in range(N-1):
    if S[-1 - i] != 1:
        S[-1 - i] = max(S[-1 - i]) + min(S[-1 - i]) + 1
    
    b = B[-1 - i] - 1
    if S[b] == 1:
        S[b] = [S[-1 - i]]
    else:
        S[b].append(S[-1 - i])
print(max(S[0]) + min(S[0]) + 1)
