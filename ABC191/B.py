N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
print(*[x for x in A if x != X])