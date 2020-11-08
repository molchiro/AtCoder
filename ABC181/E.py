from bisect import bisect_left

N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()
W.sort()
L = [0]*N
temp = H[0]
for i in range(1, N):
    L[i] = L[i-1]
    if i%2:
        L[i] += H[i]-temp
    else:
        temp = H[i]
R = [0]*N
temp = H[-1]
for i in range(N-2, -1, -1):
    R[i] = R[i+1]
    if i%2:
        R[i] += temp-H[i]
    else:
        temp = H[i]

ans = float('inf')
for w in W:
    idx = bisect_left(H, w)
    if idx == 0:
        ans = min(ans, R[0]+H[0]-w)
    elif idx == N:
        ans = min(ans, L[-1]+w-H[-1])
    else:
        if idx%2 == 1:
            idx -= 1
        ans = min(ans, L[idx]+R[idx]+abs(H[idx]-w))
print(ans)