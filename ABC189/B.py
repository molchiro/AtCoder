N, X = list(map(int, input().split()))
total_alc = 0
for i in range(N):
    V, P = list(map(int, input().split()))
    total_alc += V*P
    if total_alc > X*100:
        print(i+1)
        exit()
print(-1)