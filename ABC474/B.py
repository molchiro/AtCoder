N = int(input())
P = list(map(int, input().split()))


f = 1
for g in range(N//10+1):
    for i in range(0+g*10, min(N, (g+1)*10)):
        if (P[i]-1)//10 != g:
            f = 0

print('Yes' if f else 'No')