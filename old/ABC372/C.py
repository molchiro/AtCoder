N, Q = list(map(int, input().split()))
S = list('XX'+input()+'XX')
ans = 0
for i in range(N):
    if S[i+2:i+5] == ['A', 'B', 'C']:
        ans += 1
# print(ans)

for _ in range(Q):
    X, C = input().split()
    X = int(X)+1
    for i in range(3):
        if S[X-i:X-i+3] == ['A', 'B', 'C']:
            ans -= 1
    S[X] = C
    for i in range(3):
        if S[X-i:X-i+3] == ['A', 'B', 'C']:
            ans += 1
    
    print(ans)