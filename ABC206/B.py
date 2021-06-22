N = int(input())
ans = int((2*N)**0.5-1)
while ans*(ans+1) < 2*N:
    ans += 1
print(ans)