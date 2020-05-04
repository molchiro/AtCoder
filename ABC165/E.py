N, M = list(map(int, input().split()))
A = [i + 1 for i in range(N)]
mid = N//2
ans = []
for i in range(M+1//2):
    ans.append([A[mid - i], A[mid + 1 + i]])
    ans.append([A[-1 - i], A[1 + i]])
for i in range(M):
    print(*ans[i])