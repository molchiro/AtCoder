N, M = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(M)]
score = [-10**18]*N
score[0] = 0
for _ in range(N-1):
    for i in range(M):
        a, b, c = graph[i]
        if score[a-1]+c > score[b-1]:
            score[b-1] = score[a-1]+c
ans = score[N-1]

for _ in range(N):
    for i in range(M):
        a, b, c = graph[i]
        if score[a-1]+c > score[b-1]:
            score[b-1] = score[a-1]+c
if ans == score[N-1]:
    print(ans)
else:
    print('inf')