N, M = list(map(int, input().split()))
if M == 0:
    for i in range(N):
        print(i*2+1, i*2+2)
    exit()
elif M < 0:
    print(-1)
    exit()
elif N - M < 2:
    print(-1)
    exit()

print(1, (M+1)*2+2)
for i in range(2, (M+1)*2+2, 2):
    print(i, i+1)
for i in range(N-M-2):
    i *= 2
    i += (M+1)*2+3
    print(i, i+1)