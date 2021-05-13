N, X = list(map(int, input().split()))
s = input()
for i in range(N):
    if s[i] == 'o':
        X += 1
    else:
        X = max(0, X-1)
print(X)