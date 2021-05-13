N = int(input())
A = list(map(int, input().split()))
while True:
    tmp = []
    m = min(A)
    for a in A:
        x = a%m
        if x > 0:
            tmp.append(x)
    if tmp == []:
        break
    A = tmp
    
print(m)