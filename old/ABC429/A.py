N, M = list(map(int, input().split()))
for i in range(1, N+1):
    print('OK' if i <= M else 'Too Many Requests')