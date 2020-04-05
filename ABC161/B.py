N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
total = sum(A)
print('Yes' if len([x for x in A if x >= total/4/M]) >= M else 'No')