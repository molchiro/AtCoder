from bisect import bisect_right

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
head = [1]
n = [1]
for a in A:
    if head[-1] == a:
        head[-1] = a+1
    else:
        n.append(n[-1]+a-head[-1])
        head.append(a+1)
for _ in range(Q):
    K = int(input())
    idx = bisect_right(n, K) - 1
    print(head[idx] + K - n[idx])