N, M, K = list(map(int, input().split()))

AC = [0 for _ in range(N)]

ans = []
for _ in range(K):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    AC[A] += 1
    if AC[A] >= M:
        ans.append(A+1)
    
print(*ans)
    

