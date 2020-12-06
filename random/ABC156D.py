n, a, b = map(int, input().split())
mod = 10**9 + 7
 
def combi_mod(n, r, mod):
    numerator = 1
    denominater = 1
    for i in range(r):
        numerator = numerator * (n-i) % mod
        denominater = denominater * (i+1) % mod
    return numerator * pow(denominater, mod - 2, mod) % mod
 
print((pow(2, n, mod) -1 - combi_mod(n, a, mod) - combi_mod(n, b, mod)) % mod)