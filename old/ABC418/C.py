N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)
total = sum(A)
M = max(A)
ans = [-2]*(10**6+1)
tmp = 0
for i in range(1, 10**6+1):
    if i > M:
        break
    while A and A[-1] < i:
        # tmp += len(A)
        A.pop()

    ans[i] = tmp
    tmp += len(A)
    if tmp > total:
        break

# print(ans[:10])

for _ in range(Q):
    B = int(input())
    print(ans[B]+1)