def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N = int(input())
l = [0]*(N+1)
for i in range(2, N+1):
    for e, n in factorization(i):
        l[e] = max(l[e], n)
ans = 1
for i in range(2, N+1):
    if l[i]:
        ans *= i**l[i]
print(ans+1)