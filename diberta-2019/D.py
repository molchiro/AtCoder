N = int(input())

res = 0
for i in range(1, int((N+1)**0.5)):
    if N%i == 0 :
        res += N//i-1
print(int(res))