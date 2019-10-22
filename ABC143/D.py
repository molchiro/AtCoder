import bisect

N = int(input())
L = list(map(int, input().split()))

L.sort()

ans = 0
for i in range(N-2):
    for j in range(N-i-1):
        a = L[i]
        b = L[i+j+1]
        c_right = bisect.bisect_left(L, b + a, i+j+2)
        ans += c_right - (i+j+2)
print(ans)
