from collections import deque

def get_left(L):
    dq = deque()
    dq.append((0, -1))
    res = [i for i in range(len(L))]
    for i in range(len(L)):
        el = L[i]
        while dq[-1][0] >= el:
            dq.pop()
        dq.append((el, i))
        res[i] = dq[-2][1] + 1
    return res

def get_right(L):
    L = L[::-1]
    res = get_left(L)
    res = [len(L) - x - 1 for x in res[::-1]]
    return res

N = int(input())
A = list(map(int, input().split()))
l = get_left(A)
r = get_right(A)
ans = 0
for i in range(N):
    ans = max(ans, A[i]*(r[i]-l[i]+1))
print(ans)