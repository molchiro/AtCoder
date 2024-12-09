N = int(input())
A = list(map(tuple, enumerate(map(int, input().split()))))
A.sort(key=lambda x: x[1])
print(A[-2][0]+1)