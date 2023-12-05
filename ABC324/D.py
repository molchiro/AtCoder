N = int(input())
S = sorted(list(input()))

ans = 0

i = 0
while True:
    square = i**2
    if len(str(square)) > N:
        break
    T = sorted(list('0'*13+str(square))[::-1][:N])
    # print(T)
    if S == T:
        ans += 1
    i += 1
    
print(ans)
            
