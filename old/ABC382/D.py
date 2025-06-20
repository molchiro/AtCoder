N, M = list(map(int, input().split()))

ans = []

def create(n, accum):
    global N, M
    global ans

    if n == 0:
        ans.append(accum[:])
        return
    
    if accum[-1] + 10 > M:
        return
    
    for i in range(accum[-1]+10, M+1 - 10*(n-1)):
        create(n-1, accum[:]+[i])

for i in range(1, M+1 - 10*(N-1)):
    create(N-1, [i])

print(len(ans))
for a in ans:
    print(*a)