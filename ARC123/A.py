A1, A2, A3 = list(map(int, input().split()))
if A1 > A3:
    A1, A3 = A3, A1
ave = (A1+A3)/2
if A2 < ave:
    if (ave-A2)*2%2:
        print(int(ave-A2+1)+1)
    else:
        print(int(ave-A2))
else:
    print(int((A2-ave)*2))