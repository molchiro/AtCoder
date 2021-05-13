import heapq

X, Y, A, B, C= list(map(int, input().split()))
P = list(map(int, input().split()))
P.sort(reverse=True)
P = P[:X]
heapq.heapify(P)
Q = list(map(int, input().split()))
Q.sort(reverse=True)
Q = Q[:Y]
heapq.heapify(Q)
R = list(map(int, input().split()))
R.sort(reverse=True)
for r in R:
    p_min = P[0]
    q_min = Q[0]
    if p_min <= q_min and p_min < r:
        heapq.heapreplace(P, r)
    elif q_min <= p_min and q_min < r:
        heapq.heapreplace(Q, r)
    else:
        break
print(sum(P) + sum(Q))