N = int(input())
S = input()
T = input()



def solve(N, S, T):
    ans = 0
    accum = 0
    last_l = -1
    last_r = -1
    for i in range(N):
        s = S[i]
        t = T[i]
        if t == 'B':
            last_r = i

        if s == 'B' and t == 'A':
            ans += 1
            accum += 1
            last_l = i
        elif s == 'A' and t == 'B':
            accum -= 1
        
        if accum < 0:
            return -1
    if not last_l < last_r:
        return -1
    return ans
    

ans_1 = solve(N, S, T)
ans_2 = solve(N, T[::-1], S[::-1])

if ans_1 < 0 or ans_2 < 0:
    print(-1)
else:
    print(max(ans_1, ans_2))
