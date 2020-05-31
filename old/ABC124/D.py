def max_ones(S):
    l = []
    temp = 0
    for s in S:
        if s == '1':
            temp += 1
        else:
            l.append(temp)
            temp = 0
    l.append(temp)
    return max(l)

N, K = list(map(int, input().split()))
S = list(input())

ls_try = []

prev = '1'
for i, s in enumerate(S):
    if s == '0' and prev == '1':
        ls_try.append(i)
    prev = s

ans_try = [max_ones(S[:])]

for l_try in ls_try:
    S_copy = S[:]
    ct = 0
    prev = '1'
    for i in range(N - l_try):
        if S_copy[l_try + i] == '1' and prev == '0':
            ct += 1
        if ct >= K:
            break
        prev = S_copy[l_try + i]
        S_copy[l_try + i] = '1'

    ans_try.append(max_ones(S_copy[:]))
print(max(ans_try))
