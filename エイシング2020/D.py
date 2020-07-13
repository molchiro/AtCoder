# N = 10
# X = '1'*N
N = int(input())
X = input()
popcount_X = X.count('1')
X_ = int(X, 2)

X_mod_minus = X_%(popcount_X-1) if popcount_X > 1 else -1
X_mod_plus = X_%(popcount_X+1)
for i in range(N):
    if X[i] == '0':
        popcount = popcount_X+1
        X_i = (X_mod_plus + pow(2, N-i-1, popcount))%(popcount)
    else:
        if X_mod_minus == -1:
            print(0)
            continue
        popcount = popcount_X-1
        X_i = (X_mod_minus - pow(2, N-i-1, popcount))%(popcount)
    ans = 1
    while X_i > 0:
        X_i %= bin(X_i).count('1')
        ans += 1
    print(ans)