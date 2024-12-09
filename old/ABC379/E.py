N = int(input())
S = input()

import sys

sys.set_int_max_str_digits(10**9)
ans = []
k = 1
accum = 0

cumsum = [0]
for i in range(N):
    s = int(S[i])
    cumsum.append(cumsum[-1]+s*(i+1))

# print(cumsum)

for i in range(N):
    n = cumsum[-i-1]
    accum += n

    ans.append(accum%10)

    accum //= 10

if accum != 0:
    ans.append(accum)

print(*ans[::-1], sep='')
