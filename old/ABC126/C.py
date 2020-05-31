N, K = list(map(int, input().split()))

i = 0
L = N
res = 0
while K*2 > 1:
    if L > K:
        res += (int(L-K+1))/(2**i)
        L = int(K-0.1**9)
    i += 1
    K = K/2
print(res/N)
