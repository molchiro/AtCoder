N = int(input())
A = list(map(int, input().split()))

B = [[A[0], 1]]
for i in range(1, N):
    if A[i] == B[-1][0]:
        B[-1][1] += 1
    else:
        B.append([A[i], 1])

# print(B)

C = []

for b in B:
    if b[1] > 2:
        C.append([b[0], 2])
        C.append([b[0], 2])
    else:
        C.append(b)
# print(C)

ans = 0
l = 0
r = 0
seen = set()
b_n = len(C)
for i in range(b_n):
    if C[i][1] != 2:
        continue
    
    seen.add(C[i][0])
    l = i
    r = max(r, l)
    
    while r+1 < b_n and C[r+1][0] not in seen and C[r+1][1] == 2:
        seen.add(C[r+1][0])
        r += 1
    
    ans = max(ans, (r-l+1)*2)
    seen.remove(C[i][0])

print(ans)