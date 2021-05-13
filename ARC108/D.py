mod = 10**9+7

N = int(input())
CAA = input()
CAB = input()
CBA = input()
CBB = input()

# [長さ][AAの箇所数][ABの箇所数][BAの箇所数][BBの箇所数]
dp = [[[[[0]*1000 for _ in range(1000)] for _ in range(1000)] for _ in range(1000)] for _ in range(1001)]

dp[2][0][1][0][0]
for i in range(2, N-1):
    if CAA == 'A':
        dp[i+1][]
