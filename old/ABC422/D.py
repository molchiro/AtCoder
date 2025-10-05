N, K = list(map(int, input().split()))
M = 2**N

ans = [0]*(M)

# まずは均等に埋める
x = K//M
for i in range(M):
    ans[i] += x
    K -= x

# 余りをうまくバラして埋める
if K >= 2**(N-1):
    for i in range(2**(N-1)):
        ans[2*i+1] += 1
        K -= 1


def place(l, n, offset):
    global ans

    if n == 0:
        return
    if n == 1:
        ans[offset] += 1
        return
    
    place(l//2, n//2 + n%2, offset)
    place(l//2, n//2, offset+l//2)

place(M, K, 0)


def score(array):
    if len(array) == 2:
        return max(array) - min(array)

    return max((max(array) - min(array)), score([array[2*i] + array[2*i+1] for i in range(len(array)//2)]))

print(score(ans))
print(*ans)