N = int(input())
L = list(map(int, input().split()))
l = 0
r = N
for i in range(N):
    if L[i] == 0:
        l += 1
    else:
        break

for i in range(N-1, -1, -1):
    if L[i] == 0:
        r -= 1
    else:
        break

print(max(0, r-l-1))