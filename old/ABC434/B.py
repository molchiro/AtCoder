N, M = list(map(int, input().split()))
birds = [[] for _ in range(M)]
for _ in range(N):
    A, B = list(map(int, input().split()))
    birds[A-1].append(B)
for i in range(M):
    print(sum(birds[i])/len(birds[i]))