N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
days_remained = N - sum(A)
print(-1 if days_remained < 0 else days_remained)