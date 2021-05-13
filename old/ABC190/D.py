N = int(input())

while N%2 == 0:
    N //= 2

ans = 0
for i in range(1, int(N**0.5)+1):
    if N%i == 0:
        ans += 1
        if i*i != N:
            ans += 1
    
print(ans*2)