N = int(input())
S = input()

# 左から
cumsum_l = [0]
prev = '0'
l = N
for i in range(N):
    if prev == '1' and S[i] == '0':
        l = min(l, i)
    
    if S[i] == '1':
        cumsum_l.append(cumsum_l[-1]+1)
    else:
        cumsum_l.append(cumsum_l[-1])
    
    prev = S[i]

cumsum_l = cumsum_l[1:]

# 右から
cumsum_r = [0]
prev = '0'
r = -1
for i in range(N-1, -1, -1):
    if prev == '1' and S[i] == '0':
        r = max(r, i)
    
    if S[i] == '1':
        cumsum_r.append(cumsum_r[-1]+1)
    else:
        cumsum_r.append(cumsum_r[-1])
    
    prev = S[i]

cumsum_r = cumsum_r[1:]
cumsum_r = cumsum_r[::-1]

# print(l, cumsum_l)
# print(r, cumsum_r)

if l > r:
    print(0)
else:
    ans = 0
    for i in range(l, r+1):
        if S[i] == '1':
            continue
        ans += min(cumsum_l[i], cumsum_r[i])
    print(ans)