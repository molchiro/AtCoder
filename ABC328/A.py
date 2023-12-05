N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
print(sum([a for a in A if a <= X]))