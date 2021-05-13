N = int(input())
A = list(map(int, input().split()))
M = 0
for i in range(2, max(A)+1):
    tmp = 0
    for a in A:
        if a%i == 0:
            tmp += 1
    if tmp > M:
        M = tmp
        ans = i
print(ans)