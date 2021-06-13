N = int(input())
A = list(map(int, input().split()))
A.sort()
print('Yes' if A == [i+1 for i  in range(N)] else 'No')