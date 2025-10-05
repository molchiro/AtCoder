N, Q = list(map(int, input().split()))
X = list(map(int, input().split()))
B = [0]*N

ans = []
for x in X:
    # print(B)
    if x == 0:
        idx = 0
        m = float('inf')
        for i, b in enumerate(B):
            if b < m:
                m = b
                idx = i
        ans.append(idx+1)
        B[idx] += 1
    else:
        ans.append(x)
        B[x-1] += 1


print(*ans)
