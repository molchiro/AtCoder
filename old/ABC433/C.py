S = input()
N = len(S)
ans = 0
for i in range(N-1):
    if not int(S[i])+1 == int(S[i+1]):
        continue
    
    k = 0
    while i-k >= 0 and i+1+k < N and S[i] == S[i-k] and S[i+1] == S[i+1+k]:
        ans += 1
        k += 1

print(ans)
