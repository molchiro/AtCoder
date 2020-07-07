N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
print(sum([A[(1+i)//2] for i in range(N-1)]))