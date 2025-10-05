N, L, R = list(map(int, input().split()))
S = input()

print('Yes' if 'x' not in S[L-1:R] else 'No')