N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.append(0)
 

res = 0
for i in range(N):
    x = min(A[-1-i], B[-1-i])
    res += x
    A[-1-i] -= x
    y = min(A[-1-i], B[-2-i])
    res += y
    A[-1-i] -= y
    B[-2-i] -= y

x = min(A[0], B[0])
res += x
print(res)