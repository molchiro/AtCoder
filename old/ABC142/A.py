N = int(input())
print(len([1 for i in range(N) if (i+1)%2==1])/N)