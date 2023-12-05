import sys

sys.setrecursionlimit(10**9)

N, X, Y = list(map(int, input().split()))
# 便宜上末端でも毎秒バスが出ているものとして解く
buses = [(1, X)]
ideal_time = X + Y
for _ in range(N-1):
    P, T = list(map(int, input().split()))
    ideal_time += T
    buses.append((P, T%840))

def wait(q, p):
    if q%p==0:
        return 0
    else:
        return p-q%p

total_wait_prev = [0]*840
for i in range(N):
    p, t = buses[-i-1]
    total_wait = [ wait(i, p) + total_wait_prev[(i + wait(i, p) + t)%840] for i in range(840)]
    total_wait_prev = total_wait[:]

    # print(total_wait)

# print(ideal_time)
Q = int(input())
for _ in range(Q):
    q = int(input())
    print(q + ideal_time + total_wait[q%840])