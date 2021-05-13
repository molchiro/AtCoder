def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out

X = int(input())
M = int(input())

if len(str(X)) == 1:
    print(int(X<=M))
    exit()

ans = 0
s = max([int(x) for x in str(X)])

l = s
r = 2*s
while Base_n_to_10(str(X), r) <= M:
    l = r
    r *= 2

while l+1 < r:
    m = (l+r)//2
    if Base_n_to_10(str(X), m) <= M:
        l = m
    else:
        r = m

print(l-s)