N, K = list(map(int, input().split()))
S = input()
pre = '1'
l = []
l.append(0)
for i, s in enumerate(S):
    if s != pre:
        l.append(i)
    pre = s
l.append(N)
if S[-1] == '0':
    l.append(N)
if len(l) <= 2*K+1:
    print(N)
else:
    ans = 0
    for i in range(0, len(l)-2*K-1, 2):
        ans = max(ans, l[i+2*K+1]-l[i])
    print(ans)