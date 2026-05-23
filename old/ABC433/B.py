N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    ans = -1
    for j in range(i):
        if A[j] > A[i]:
            ans = j+1
    print(ans) 