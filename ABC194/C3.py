N = int(input())
A = list(map(int, input().split()))
print(N*sum([x**2 for x in A]) - sum(A)**2)