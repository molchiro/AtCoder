import sys

sys.set_int_max_str_digits(10**9)

N = 2*(10**5)
S = '1'*N

ans = 0
k = 1

for i in range(N):
    s = int(S[-i-1])

    ans += (N-i)*s*k
    k *= 10
    k += 1

print(ans)