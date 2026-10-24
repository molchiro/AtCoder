N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

accum = 0
s = set([0])
ans = 0

for a in A:
    accum += a
    accum %= K
    # print(ans, accum, s)
    if accum in s:
        ans += 1
        s = set([0])
        accum = 0
    else:
        s.add(accum)

print(ans)