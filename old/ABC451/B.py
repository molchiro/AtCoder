N, M = list(map(int, input().split()))
now = [0]*M
nxt = [0]*M

for _ in range(N):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    now[A] += 1
    nxt[B] += 1

for i in range(M):
    print(nxt[i]-now[i])