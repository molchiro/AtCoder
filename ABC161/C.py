N, K = list(map(int, input().split()))
rem = N%K
print(min(rem, abs(K-rem)))