N, H, X = list(map(int, input().split()))
P = list(map(int, input().split()))
for i in range(N):
    if P[i] + H >= X:
        print(i+1)
        break
