from atcoder.math import floor_sum
T = int(input())
for _ in range(T):
    N, M, A, B = list(map(int, input().split()))
    print(floor_sum(N, M, A, B))