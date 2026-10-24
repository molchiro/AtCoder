T = int(input())
for _ in range(T):
    X1, Y1, R1, X2, Y2, R2 = list(map(int, input().split()))
    print('Yes' if (R1-R2)**2 <= (X2-X1)**2 + (Y2-Y1)**2 <= (R1+R2)**2 else 'No')