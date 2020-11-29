n = int(input())

l = 1
r = n+1
while r - l > 1:
    mid = (l+r)//2
    if mid*(mid+1)//2 > n+1:
        r = mid
    else:
        l = mid

print(n+1-l)