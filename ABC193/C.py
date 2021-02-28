N = int(input())
rN = int(N**0.5)
ans = N
seen = [0]*(rN+1)
for i in range(2, rN+1):
    if seen[i] == 1:
        continue

    j = 2
    tmp = i**j
    while tmp <= rN:
        seen[tmp] = 1
        tmp *= i
        j += 1
    while tmp <= N:
        tmp *= i
        j += 1
    
    ans -= j-2

print(ans)
