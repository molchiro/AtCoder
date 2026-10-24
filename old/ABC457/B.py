N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
X, Y = list(map(lambda x: int(x) - 1, input().split()))
print(A[X][Y+1])