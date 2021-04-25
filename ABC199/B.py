N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(max(-1, min(B)-max(A))+1)