INF = 1001001001
N, Q = list(map(int, input().split()))
school = [[0]*N for _ in range(200000)]
infants = [0]*N
for i in range(N):
    A, B = list(map(int, input().split()))
    infants[i] = A
    school[B-1][i] = 1
highest = [INF]*(200000)



print(min(highest))