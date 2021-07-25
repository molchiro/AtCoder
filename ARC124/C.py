def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp

    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b

def lcm(a, b):
    return int(a * b / gcd(a, b))


N = int(input())
pairs = set()
a, b = list(map(int, input().split()))
if a > b:
    a, b = b, a
pairs.add((a, b))
for _ in range(N-1):
    next_pairs = set()
    a_1, b_1 = list(map(int, input().split()))
    for a_2, b_2 in pairs:
        a_3, b_3 = gcd(a_1, a_2), gcd(b_1, b_2)
        if a_3 > b_3:
            a_3, b_3 = b_3, a_3
        next_pairs.add((a_3, b_3))
        a_3, b_3 = gcd(a_1, b_2), gcd(b_1, a_2)
        if a_3 > b_3:
            a_3, b_3 = b_3, a_3
        next_pairs.add((a_3, b_3))
    pairs = next_pairs
    # print('hige', len(pairs), pairs)
ans = 0
for a, b in pairs:
    ans = max(ans, lcm(a, b))
print(ans)