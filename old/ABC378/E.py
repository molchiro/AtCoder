from itertools import accumulate

def cumsum(input_list, mod=None, initial=None):
    func = (lambda x, y: x+y) if (mod == None) else (lambda x, y: (x+y)%mod)
    return list(accumulate(input_list, func=func, initial=initial))

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

S = cumsum(A, mod=M, initial=0)
T = cumsum(S, mod=M)

print(S)
print(T)

ans = 0
for i in range(N):
    ans += ((T[-1]-T[i]) - (N-i)*S[i])%M
print(ans)