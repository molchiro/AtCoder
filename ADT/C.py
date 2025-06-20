N, Q = list(map(int, input().split()))
hoge = [list(map(int, input().split())) for _ in range(N)]
for _ in range(Q):
    s, t = list(map(int, input().split()))
    print(hoge[s-1][t])