H1, M1, H2, M2, K = list(map(int, input().split()))
print(H2*60 + M2 - K - H1*60 - M1)