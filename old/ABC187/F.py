N, M = list(map(int, input().split()))
connection = [[0]*18 for _ in range(18)]
fixed = [False]*18

for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    connection[A][B] = 1
    connection[B][A] = 1

