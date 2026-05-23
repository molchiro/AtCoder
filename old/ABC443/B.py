N, K = list(map(int, input().split()))

tmp = 0
ct = 0
while tmp < K:
    tmp += N
    N += 1
    ct += 1
print(ct-1)