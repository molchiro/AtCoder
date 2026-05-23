N, M = list(map(int, input().split()))
l = [0]*N
for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    l[A] += 1
    l[B] += 1

ans = [int(max(0, (N-1-l[i])*(N-1-l[i]-1)*(N-1-l[i]-2)/6)) for i in range(N)]
print(*ans)