N = int(input())
ans = float('inf')
b = 0
while 2**b <= N:
    a = N//(2**b)
    c = N - a*2**b
    ans = min(ans, a+b+c)
    b += 1
print(ans)