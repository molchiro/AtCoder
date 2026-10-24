N, M = list(map(int, input().split()))
ans = [0]*N
for i in range(M):
    ans[i%N] += 1

print(*ans, sep='\n')