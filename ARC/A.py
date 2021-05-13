N, M = list(map(int, input().split()))

seen = [0]*(M+1)
i = 0
tmp = 1
while i <= N:
    tmp *= 10
    mod = (tmp//M)%M
    if seen[mod]:
        print(tmp, i, mod)
        exit()
    seen[mod] = 1
    i += 1

print(mod)