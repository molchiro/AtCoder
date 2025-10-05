N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
idx = 0
for i in range(101):
    while idx < N and A[idx] < i:
        idx += 1
    # print(idx, i, A[i])
    if N-idx >= i:
        # print(N-idx, i)
        ans = i

print(ans)