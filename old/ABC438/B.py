N, M = list(map(int, input().split()))
S = input()
T = input()

def culc(s, t):
    # print(s, t)
    res = 0
    for a, b in zip(s, t):
        a = int(a)
        b = int(b)
        if a < b:
            a += 10
        res += a-b
    return res

ans = 10**18
for i in range(N-M+1):
    s = S[i:i+M]
    ans = min(ans, culc(s, T))
print(ans)