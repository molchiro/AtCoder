T = int(input())
for _ in range(T):
    a, s = list(map(int, input().split()))
    s -= 2*a
    print('Yes' if s >= 0 else 'No')
