N, K = list(map(int, input().split()))
S = input()
accum = 0

ans = 0
for i in range(N):
    if S[i] == 'O':
        accum += 1
    else:
        accum = 0
    
    # print(accum)

    if accum == K:
        ans += 1
        accum = 0
    
print(ans)