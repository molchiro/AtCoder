S = input()
A = S.split('|')
print(*[len(a) for a in A[1: len(A)-1]])