N = int(input())
A = list(map(int, input().split()))
AA = [a**2 for a in A]
accum_A = sum(A)
accum_AA = sum(AA)
ans = 0
for i in range(N-1):
    accum_A -= A[i]
    accum_AA -= AA[i]
    ans += AA[i]*(N-1-i)
    ans += accum_AA
    ans -= 2*A[i]*accum_A
    # print(ans)
print(ans)