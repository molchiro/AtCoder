N, K = list(map(int, input().split()))
S = input()

from itertools import permutations
def is_kaibun(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

ans = 0
for s in permutations(list(S)):
    # print(s)
    f = 1
    for i in range(N-K+1):
        # print(s[i:i+K])
        if is_kaibun(s[i:i+K]):
            f = 0
    ans += f

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# print(ans)

for i in range(26):
    n = S.count(chr(i+ord('a')))
    ans //= factorial(n)

print(ans)