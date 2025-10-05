from collections import Counter
from copy import deepcopy

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

prime_f_counter = [Counter()]

for i in range(1, 5001):
    prime_f_counter.append(Counter(prime_factorize(i)) + prime_f_counter[-1])

T, M = [1, 10**18]
for _ in range(T):
    N = 1
    C = [1]*5000
    counter = deepcopy(prime_f_counter[sum(C)])
    for c in C:
        counter -= prime_f_counter[c]
    # print(counter)
    
    ans = 1
    for k, v in counter.items():
        ans *= k**v
        ans %= M
    
    print(ans)


# T, M = list(map(int, input().split()))
# for _ in range(T):
#     N = int(input())
#     C = list(map(int, input().split()))
#     counter = deepcopy(prime_f_counter[sum(C)])
#     for c in C:
#         counter -= prime_f_counter[c]
#     # print(counter)
    
#     ans = 1
#     for k, v in counter.items():
#         ans *= k**v
#         ans %= M
    
#     print(ans)
    

    
