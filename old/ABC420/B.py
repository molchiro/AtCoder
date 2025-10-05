N, M = list(map(int, input().split()))
tokuten = [0]*N
S = [input() for _ in range(N)]
for i in range(M):
    vote = [s[i] for s in S]
    if vote.count('1') > N//2:
        for j in range(N):
            if vote[j] == '0':
                tokuten[j] += 1
    else:
        for j in range(N):
            if vote[j] == '1':
                tokuten[j] += 1

largest = max(tokuten)

ans = []
for i in range(N):
    if tokuten[i] == largest:
        ans.append(i+1)
print(*ans)