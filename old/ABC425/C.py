N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1]+a)
for a in A:
    cumsum.append(cumsum[-1]+a)

offset = 0

for _ in range(Q):
    t, *args = list(map(int, input().split()))
    if t == 1:
        c = args[0]
        offset += c
        offset %= N
    else:
        l, r = args
        print(cumsum[r+offset] - cumsum[l+offset-1]) 