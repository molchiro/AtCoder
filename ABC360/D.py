N, T = list(map(int, input().split()))
S = input()
X = list(map(int, input().split()))
R = []
L = []
for i, s in enumerate(S):
    if s == '1':
        R.append(X[i])
    else:
        L.append(X[i])
    
R.sort()
L.sort()
R_n = len(R)
L_n = len(L)

ans = 0
l = 0
r = 0

# print(R)
# print(L)

for x in R:
    while l < L_n and x > L[l]:
        l += 1
    while r < L_n and x+2*T >= L[r]:
        r += 1
    ans += r-l
    # print(ans)
    # input()

print(ans)