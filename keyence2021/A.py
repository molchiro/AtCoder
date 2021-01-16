N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ab_max = 0
a_max = 0

for i in range(N):
    a_max = max(a_max, A[i])
    ab_max = max(ab_max, a_max*B[i])
    print(ab_max)