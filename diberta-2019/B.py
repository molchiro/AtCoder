INPUT = list(map(int, input().split()))

N = INPUT.pop(3)
INPUT.sort()

res = 0
for i in range(N//INPUT[2]+1):
    remainder_1 = N-INPUT[2]*i
    for j in range(remainder_1//INPUT[1]+1):
        remainder_2 = remainder_1-INPUT[1]*j
        if remainder_2%INPUT[0] == 0:
            res += 1

print(res)