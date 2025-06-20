N = int(input())
S = input()
S = 'x' + S + 'x'

ans = 1
for i in range(1, N+1):
    if S[i] != '/':
        continue

    tmp = 0
    while S[i-tmp-1] == '1' and S[i+tmp+1] == '2':
        tmp += 1
    
    ans = max(ans, tmp*2+1)

print(ans)