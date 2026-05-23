N, L, R = list(map(int, input().split()))
S = input()
ans = 0
for i in range(26):
    c = chr(ord('a')+i)
    T = [int(s==c) for s in S]
    # print(T)
    accum = 0
    for j in range(L, R+1):
        accum += T[j]
    # print(accum)
    for j in range(N-L):
        # print((j, j+L, j+R), accum)
        if T[j]:
            ans += accum
        
        if j+R+1 < N:
            accum += T[j+R+1]
        
        if j+L < N:
            accum -= T[j+L]
    # print(ans)

print(ans)