N = int(input())
if N < 1000:
    print(0)
    exit()
ans = 0
i = 1
while 1000**(i+1) <= N:
    
    ans += i*(1000**(i+1)-1000**i)
    i += 1
ans += i*(N-1000**i+1)
print(ans)