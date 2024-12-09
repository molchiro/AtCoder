N, T, A = list(map(int, input().split()))
rem = N - T - A

print('Yes' if rem < abs(T-A) else 'No')