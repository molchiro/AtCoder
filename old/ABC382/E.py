
N, X = list(map(int, input().split()))
P = list(map(int, input().split()))
P_S = sum([p/100 for p in P])
print(P_S)

# パックに入っているレアの枚数がn枚の確率
Q = [0]*(N+1)
ncr = 1
for i in range(1, N):
    ncr *= N-i
    ncr //= i
    Q[i] = i*ncr*((N-1-i)*i*P_S+(N-P_S))
Q[N] = P_S

print(*Q)

# from functools import cache

# @cache
# def solve(x):
#     global N, X, P

    



#     return

# print(solve(X))