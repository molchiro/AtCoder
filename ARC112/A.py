T = int(input())
for _ in range(T):
    L, R = list(map(int, input().split()))
    if 2*L <= R:
        print((R-2*L+2)*(R-2*L+1)//2)
    else:
        print(0)
