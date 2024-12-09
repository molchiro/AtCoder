N = int(input())

if N <= 10:
    print(N-1)
    exit()

N -= 10
digit = 2
while N - (10**((digit+1)//2)-10**((digit+1)//2-1)) > 0:
    # print(N ,10**((digit+1)//2)-10**((digit+1)//2-1))
    # input()
    N -= (10**((digit+1)//2)-10**((digit+1)//2-1))
    digit += 1

# print(N, digit)
S = 10**((digit+1)//2-1) + N - 1
S = str(S)
# print(S)
if digit%2:
    print(S+S[digit//2-1::-1])
else:
    print(S+S[::-1])