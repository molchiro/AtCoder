N, A, B = list(map(int, input().split()))
ans = []
for i in range(N*A):
    ans.append([])
    for j in range(N*B):
        if (i//A)%2 and not (j//B)%2:

            ans[-1].append('#')
        elif not (i//A)%2 and (j//B)%2:
        
            ans[-1].append('#')
        elif (i//A)%2 and (j//B)%2:

            ans[-1].append('.')
        else:
            ans[-1].append('.')
print(*[''.join(x) for x in ans], sep='\n')