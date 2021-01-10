from math import gcd

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
two_n = 0
f = True
while True:
    tmp = A[0]%2
    two_n += 1
    A = [a//2 for a in A]
    A_next_rem = [a%2 for a in A]
    if len(set(A_next_rem)) == 2:
        f = False
        break
    else:
        if A_next_rem[0] == 1:
            break

if f:
    lcm = 1
    for a in A:
        lcm = lcm*a//gcd(lcm, a)
    lcm *= 2**(two_n-1)
    print((M-lcm)//(lcm*2)+1)
else:
    print(0)