N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)

skipped = 0
ans = None
for i in range(N-1):
    if not skipped and A[i] > B[i]:
        ans = A[i]
        skipped = 1
    if skipped:
        if A[i+1] > B[i]:
            print(-1)
            exit()

if ans == None:
    print(A[-1])
else:
    print(ans)