N = int(input())
A = list(map(int, input().split()))
A_set = set(A)
print(sorted(list(A_set))[-2])