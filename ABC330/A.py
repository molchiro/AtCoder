N, L = list(map(int, input().split()))
A = list(map(int, input().split()))
print(len([a for a in A if a >= L]))